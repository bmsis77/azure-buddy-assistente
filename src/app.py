import re
from pathlib import Path

import streamlit as st


# ==============================
# CONFIGURAÇÃO
# ==============================

st.set_page_config(
    page_title="Azure Buddy",
    page_icon="☁️",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_BASE = BASE_DIR / "data" / "azure_basico.md"


# ==============================
# CARREGAR BASE DE CONHECIMENTO
# ==============================

with open(ARQUIVO_BASE, "r", encoding="utf-8") as arquivo:
    base_conhecimento = arquivo.read()


# ==============================
# ORGANIZAR A BASE
# ==============================

def carregar_secoes(texto):
    secoes = {}
    secao_atual = "Geral"

    for linha in texto.splitlines():

        if linha.startswith("## "):
            secao_atual = linha.replace("## ", "").strip()

            # Remove a numeração do título.
            # Exemplo: "1. Microsoft Azure" -> "Microsoft Azure"
            secao_atual = re.sub(r"^\d+\.\s*", "", secao_atual)

            secoes[secao_atual] = []

        elif secao_atual in secoes:
            secoes[secao_atual].append(linha)

    return {
        nome: "\n".join(conteudo).strip()
        for nome, conteudo in secoes.items()
    }


secoes = carregar_secoes(base_conhecimento)


# ==============================
# BUSCA NA BASE
# ==============================

def normalizar(texto):
    texto = texto.lower()

    substituicoes = {
        "á": "a",
        "à": "a",
        "ã": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "ç": "c",
    }

    for original, substituto in substituicoes.items():
        texto = texto.replace(original, substituto)

    return texto


def buscar_resposta(pergunta):
    pergunta_normalizada = normalizar(pergunta)

    palavras_chave = {
        "microsoft azure": "Microsoft Azure",
        "azure": "Microsoft Azure",
        "computacao em nuvem": "Computação em Nuvem",
        "nuvem": "Computação em Nuvem",
        "iaas": "IaaS",
        "paas": "PaaS",
        "saas": "SaaS",
        "maquinas virtuais": "Azure Virtual Machines",
        "maquina virtual": "Azure Virtual Machines",
        "virtual machine": "Azure Virtual Machines",
        "app service": "Azure App Service",
        "blob storage": "Azure Blob Storage",
        "blob": "Azure Blob Storage",
        "azure files": "Azure Files",
        "entra id": "Microsoft Entra ID",
        "azure monitor": "Azure Monitor",
        "monitor": "Azure Monitor",
        "virtual network": "Azure Virtual Network",
        "rede virtual": "Azure Virtual Network",
    }

    secao_encontrada = None

    for palavra, secao in palavras_chave.items():
        if palavra in pergunta_normalizada:
            secao_encontrada = secao
            break

    if secao_encontrada and secao_encontrada in secoes:
        return (
            f"### {secao_encontrada}\n\n"
            f"{secoes[secao_encontrada]}"
        )

    return (
        "Não encontrei informações suficientes sobre esse assunto "
        "na minha base de conhecimento."
    )


# ==============================
# INTERFACE
# ==============================

st.title("☁️ Azure Buddy")

st.subheader("Seu assistente de Azure para iniciantes")

st.write(
    "Faça uma pergunta sobre conceitos fundamentais "
    "do Microsoft Azure."
)


# ==============================
# HISTÓRICO
# ==============================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])


# ==============================
# CHAT
# ==============================

pergunta = st.chat_input(
    "Digite sua dúvida sobre Azure..."
)


if pergunta:

    with st.chat_message("user"):
        st.markdown(pergunta)

    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    resposta = buscar_resposta(pergunta)

    with st.chat_message("assistant"):
        st.markdown(resposta)

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )