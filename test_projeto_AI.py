import unittest
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location(
    "projeto_ai",
    Path(__file__).resolve().parent / "projeto AI.py"
)
projeto_ai = importlib.util.module_from_spec(spec)
spec.loader.exec_module(projeto_ai)


class TestCalcularDesconto(unittest.TestCase):
    def test_pagamento_dinheiro_aplica_10_percent(self):
        desconto, forma, juros = projeto_ai.calcular_desconto(100.0, "dinheiro")
        self.assertEqual(desconto, 0.10)
        self.assertEqual(forma, "Dinheiro")
        self.assertEqual(juros, 0.0)

    def test_pagamento_pix_aplica_10_percent(self):
        desconto, forma, juros = projeto_ai.calcular_desconto(100.0, "pix")
        self.assertEqual(desconto, 0.10)
        self.assertEqual(forma, "Pix")
        self.assertEqual(juros, 0.0)

    def test_pagamento_cartao_sem_juros_ate_10_parcelas(self):
        desconto, forma, juros = projeto_ai.calcular_desconto(100.0, "cartao", parcelas=10)
        self.assertEqual(desconto, 0.00)
        self.assertEqual(forma, "Cartão")
        self.assertEqual(juros, 0.0)

    def test_pagamento_cartao_com_juros_acima_de_10_parcelas(self):
        desconto, forma, juros = projeto_ai.calcular_desconto(100.0, "cartao", parcelas=12)
        self.assertEqual(desconto, 0.00)
        self.assertEqual(forma, "Cartão")
        self.assertEqual(juros, 0.01)

    def test_metodo_invalido_nao_aplica_desconto(self):
        desconto, forma, juros = projeto_ai.calcular_desconto(100.0, "boleto")
        self.assertEqual(desconto, 0.00)
        self.assertEqual(forma, "Outro")
        self.assertEqual(juros, 0.0)


if __name__ == "__main__":
    unittest.main()
