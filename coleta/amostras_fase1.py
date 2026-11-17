#!/usr/bin/env python3
"""Gera as amostras pequenas da Fase 1 em dados/brutos/amostras/camara/.

Só Python padrão. Faz poucos pedidos à API do Portal Legislativo, com 2 segundos
entre eles, e salva APENAS os campos da lista permitida (docs/02, seção 2.1).
CPF, e-mail, telefone, nascimento e biografia nunca são pedidos nem salvos.
Não é o coletor da Fase 2: serve para conferir o formato das respostas.

Uso: python3 coleta/amostras_fase1.py
"""
import json
import re
import ssl
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://cmpelotas.cittatec.com.br/api/open-data-leg/public/"
GRAPHQL = BASE + "graphql"
UA = "MeuVereadorBot/0.1 (+https://github.com/hstreck/meu-vereador; meuvereadorrs@gmail.com)"
PAUSA = 2.0
DESTINO = Path(__file__).resolve().parent.parent / "dados" / "brutos" / "amostras" / "camara"
PROIBIDOS = {"documento", "email", "fone", "nascimento", "cpf", "biografia"}


def agora():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def limpar(o):
    """Remove qualquer campo proibido, em qualquer nível (defesa extra)."""
    if isinstance(o, dict):
        return {k: limpar(v) for k, v in o.items() if k not in PROIBIDOS}
    if isinstance(o, list):
        return [limpar(x) for x in o]
    return o


def _abrir(req):
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
        dados = json.loads(r.read().decode("utf-8"))
    time.sleep(PAUSA)
    return dados


def graphql(consulta):
    corpo = json.dumps({"query": consulta}).encode()
    req = urllib.request.Request(
        GRAPHQL, data=corpo,
        headers={"Content-Type": "application/json", "ID-Tenant": "cmpelotas", "User-Agent": UA},
    )
    resp = _abrir(req)
    if resp.get("errors"):
        raise RuntimeError(resp["errors"][0]["message"])
    return resp["data"]


def rest(caminho):
    req = urllib.request.Request(BASE + caminho, headers={"ID-Tenant": "cmpelotas", "User-Agent": UA})
    return limpar(_abrir(req))


def salvar(nome, fonte_url, dados, observacao=""):
    DESTINO.mkdir(parents=True, exist_ok=True)
    pacote = {"fonte_url": fonte_url, "coletado_em": agora(), "observacao": observacao, "dados": dados}
    (DESTINO / nome).write_text(json.dumps(pacote, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("salvo", nome)


def proposicoes():
    campos = ("id resultadoVotacao{name} processo{ id titulo descricao nroDocumento anoDocumento "
              "dataProtocolo dataPublicacao classificacao{id descricao} status{name description} "
              "statusTramitacao{name description} autores{ id nome participacao{name} } }")
    saida = []
    for classe, ano in ((25, 2025), (34, 2026), (33, 2026), (270, 2025), (31, 2026)):
        q = ('{ proposicoes(page:0,size:2,filters:[{key:ANO_DOCUMENTO,value:"%d"},'
             '{key:CLASSIFICACAO,value:"%d"}]) { %s } }' % (ano, classe, campos))
        saida += graphql(q)["proposicoes"]
    for item in saida:
        item["processo"]["descricao"] = " ".join((item["processo"]["descricao"] or "").split())[:400]
    salvar("proposicoes_amostra.json", BASE + "graphql (consulta proposicoes)", saida,
           "2 itens de cada tipo: PL ordinário 2025, pedido de informações 2026, pedido de providências 2026, "
           "emenda impositiva 2025, moção 2026. Descrições cortadas em 400 caracteres.")


def sessoes_e_presenca():
    q = ('{ sessoes(page:0,size:5,filters:[{key:ANO,value:"2026"}]) { id dataSessao inicio fim '
         'tipoSessao{ id classificacao{descricao} contabilizaFrequencia } status{ name } } }')
    sess = graphql(q)["sessoes"]
    salvar("sessoes_amostra.json", BASE + "graphql (consulta sessoes)", sess)
    q = ('{ parlamentaresSessao(page:0,size:50,filters:[{key:"ID_SESSAO",value:"545003"}]) '
         '{ id estevePresente pessoa{ id nome } partido{ sigla } cargo{ name } } }')
    salvar("presenca_sessao_545003.json", BASE + "graphql (consulta parlamentaresSessao, sessão 545003, 20/10/2026)",
           graphql(q)["parlamentaresSessao"])


def votos_e_oradores():
    votos = rest("votacoes-parlamentares/5095/votos")
    enxuto = {
        "votacao": {k: votos[0]["votacao"].get(k) for k in
                    ("id", "titulo", "inicio", "fim", "favoraveis", "contrarios", "abstidos", "ausentes",
                     "impedidos", "secreta", "simbolica", "status")},
        "resultado": votos[0]["votacao"]["resultado"]["name"],
        "sessao_id": votos[0]["parlamentar"]["sessaoPlenaria"]["id"],
        "votos": [{"pessoa_id": v["parlamentar"]["idPessoa"], "voto": v["voto"]["name"],
                   "esteve_presente": v["parlamentar"]["estevePresente"]} for v in votos],
    }
    salvar("votacao_5095.json", BASE + "votacoes-parlamentares/5095/votos", enxuto,
           "Pedido de Informações nº 1014/2026, sessão de 05/11/2026. AUSENTE no voto não é o mesmo que falta na sessão.")
    orad = rest("discussoes/4000/oradores")
    enxuto = [{"discussao_id": o["discussao"]["id"], "pessoa_id": o["idPessoa"], "ordem": o.get("ordem"),
               "inicio": o.get("inicio"), "fim": o.get("fim"),
               "segundos_concedidos": o.get("segundosConcedidos"), "segundos_discutidos": o.get("segundosDiscutidos"),
               "assunto": o.get("assunto")} for o in orad]
    salvar("oradores_discussao_4000.json", BASE + "discussoes/4000/oradores", enxuto,
           "Discussão de 17/06/2025. O campo assunto veio vazio em todas as amostras.")


def vereadores():
    """Lista dos 21 vereadores a partir da página inicial da Câmara (nome, partido, cargo, id da pessoa)."""
    req = urllib.request.Request("https://www.pelotas.rs.leg.br/", headers={"User-Agent": UA})
    html = _abrir_texto(req)
    achados = re.findall(
        r'href="https://cmpelotas\.cittatec\.com\.br/portal-legislativo/vereadores/pessoas/(\d+)"[^>]*>(.*?)</a>',
        html, re.S)
    saida = []
    for pid, bruto in achados:
        texto = " ".join(re.sub(r"<[^>]+>", " ", bruto).split())
        m = re.match(r"(.+?) --> (.+)", texto)
        if m:
            saida.append({"pessoa_id": int(pid), "partido": m.group(1), "cargo_e_nome_parlamentar": m.group(2)})
    salvar("vereadores_pagina_inicial.json", "https://www.pelotas.rs.leg.br/", saida,
           "Lido do HTML da página inicial da Câmara. O nome civil vem da API (Pessoa.nome).")


def _abrir_texto(req):
    with urllib.request.urlopen(req, context=ssl.create_default_context(), timeout=60) as r:
        texto = r.read().decode("utf-8", errors="replace")
    time.sleep(PAUSA)
    return texto


if __name__ == "__main__":
    proposicoes()
    sessoes_e_presenca()
    votos_e_oradores()
    vereadores()
