import json
import pandas as pd
import requests
import streamlit as st

# ==================== CONFIGURAÇÃO OLLA(local) ====================
# baixar o OLLAM e localizar no processo de instalação a porta que foi utilizada e o modelo que foi instalado
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"


# ==================== CARREGAR DADOS ====================
perfil = json.load(open('./data/perfil_nvestidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ==================== MONTAR CONTEXTO ====================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSAÇÔES RECENTES:
{transacoes.to_string(index=false)}
ATENDIMENTOS ANTERIORES:
{historico.to_string(index=false)}
PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=false)}
"""

# ==================== SYSTEM PROMPT ====================

SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável e didático. 
OBJETIVO: 
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.
REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema de ensino de finanças pessoais. 
Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 03 parágrafos.
 """

# ==================== CHAMAR OLLAMA ====================
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    Pergunta: msg{}"""contexto
    r = requests.post(OLLAMA_URL, json={"model":MODELO, "prompt": prompt, "stream":False})
    return r.json()['response']

# ==================== INTERFACE ====================
st.title(" Edu, seu educador financeiro")
if pergunta:= st.chat_input("Sua dúvida sobre dinanças ....."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
