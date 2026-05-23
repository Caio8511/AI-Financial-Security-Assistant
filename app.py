import streamlit as st
from services.security_service import analyze_security
from utils.logger import save_log

# Configuração da página
st.set_page_config(page_title="AI Financial Security Assistant", page_icon="🔐", layout="centered")

# Título principal
st.title("🔐 AI Financial Security Assistant")

# Descrição
st.markdown(
    """Assistente inteligente focado em:

- Segurança Financeira
- Inteligência Artificial
- Detecção de Golpes
- Automação
- Análise de Risco
"""
)

# Campo de entrada
user_input = st.text_area(
    "Digite uma dúvida ou situação suspeita:",
    placeholder="Ex: Recebi um SMS do banco pedindo minha senha...",
)


if st.button("Analisar"):
    if user_input:
        level, message = analyze_security(user_input)
        save_log(level, user_input)
        if level == "error":
            st.error(message)
        elif level == "warning":
            st.warning(message)
        else:
            st.success(message)
    else:
        st.info("Digite alguma informação para análise.")
