def analyze_security(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = text.lower()
    if "senha" in t:
        return "error", (
            "⚠️ ALERTA DE SEGURANÇA\n\n"
            "Nunca compartilhe senhas bancárias.\n\n"
            "Possível tentativa de:\n"
            "- phishing\n"
            "- engenharia social\n"
            "- fraude financeira"
        )

    if "pix" in t:
        return "warning", (
            "⚠️ CUIDADO COM GOLPES VIA PIX\n\n"
            "Verifique:\n"
            "- nome do destinatário\n"
            "- chave PIX\n"
            "- mensagens urgentes"
        )

    return "success", (
        "✅ Situação analisada.\n\n"
        "Recomendações:\n"
        "- verificar origem da mensagem\n"
        "- evitar links desconhecidos\n"
        "- confirmar informações com o banco"
    )
