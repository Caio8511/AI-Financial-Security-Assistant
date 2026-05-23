import unittest

from services.security_service import analyze_security


class TestAnalyzeSecurity(unittest.TestCase):
    def test_returns_error_for_senha(self):
        status, message = analyze_security("Por favor, me envie sua senha bancária.")
        self.assertEqual(status, "error")
        self.assertIn("Nunca compartilhe senhas bancárias", message)

    def test_returns_warning_for_pix(self):
        status, message = analyze_security("Verifique a chave PIX antes de transferir.")
        self.assertEqual(status, "warning")
        self.assertIn("CUIDADO COM GOLPES VIA PIX", message)

    def test_returns_success_for_other_input(self):
        status, message = analyze_security("Recebi um e-mail pedindo para confirmar meus dados.")
        self.assertEqual(status, "success")
        self.assertIn("Situação analisada", message)

    def test_raises_type_error_for_non_string(self):
        with self.assertRaises(TypeError):
            analyze_security(None)


if __name__ == "__main__":
    unittest.main()
