"""Verificações automáticas das amostras da Fase 1 (só Python padrão).

Rodar na raiz do repositório:  python3 -m unittest discover -s testes -v

1. Nenhum arquivo em dados/ pode conter CPF, telefone ou e-mail (docs/02, seção 2.1; 01, D16).
2. Toda amostra tem fonte_url e coletado_em (CLAUDE.md, regras de conteúdo).
3. Nenhuma amostra tem chave de campo proibido (documento, email, fone, nascimento, cpf).
"""
import json
import re
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "dados"

CPF_FORMATADO = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
CPF_11_DIGITOS = re.compile(r"(?<![\d.,])\d{11}(?![\d.,])")
TELEFONE = re.compile(r"(\(\d{2}\)\s?\d{4,5}-?\d{4}|\b\d{2}\s?9?\d{4}-\d{4}\b)")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
CHAVES_PROIBIDAS = {"documento", "email", "fone", "nascimento", "cpf", "biografia"}


def arquivos_de_dados():
    return [p for p in DADOS.rglob("*") if p.is_file() and p.suffix in {".json", ".csv", ".jsonl", ".txt"}]


def chaves(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from chaves(v)
    elif isinstance(o, list):
        for x in o:
            yield from chaves(x)


class TestDadosPessoais(unittest.TestCase):
    def test_sem_cpf_telefone_email(self):
        for p in arquivos_de_dados():
            texto = p.read_text(encoding="utf-8", errors="replace")
            for nome, padrao in (("CPF", CPF_FORMATADO), ("CPF sem pontos", CPF_11_DIGITOS),
                                 ("telefone", TELEFONE), ("e-mail", EMAIL)):
                achado = padrao.search(texto)
                self.assertIsNone(achado, f"{p.relative_to(RAIZ)}: parece conter {nome}")

    def test_sem_chaves_proibidas(self):
        for p in arquivos_de_dados():
            if p.suffix == ".json":
                dados = json.loads(p.read_text(encoding="utf-8"))
                proibidas = CHAVES_PROIBIDAS & set(chaves(dados))
                self.assertFalse(proibidas, f"{p.relative_to(RAIZ)}: campos proibidos {sorted(proibidas)}")


class TestFonteEData(unittest.TestCase):
    def test_amostras_tem_fonte_e_data(self):
        amostras = list((DADOS / "brutos" / "amostras").rglob("*.json"))
        self.assertTrue(amostras, "nenhuma amostra encontrada")
        for p in amostras:
            pacote = json.loads(p.read_text(encoding="utf-8"))
            for campo in ("fonte_url", "coletado_em", "dados"):
                self.assertIn(campo, pacote, f"{p.relative_to(RAIZ)}: falta {campo}")
            self.assertRegex(pacote["coletado_em"], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
            self.assertTrue(pacote["fonte_url"].startswith("http"))

    def test_trinta_votos_ou_menos_por_amostra_de_votacao(self):
        p = DADOS / "brutos" / "amostras" / "camara" / "votacao_5095.json"
        pacote = json.loads(p.read_text(encoding="utf-8"))
        self.assertLessEqual(len(pacote["dados"]["votos"]), 30)


if __name__ == "__main__":
    unittest.main()
