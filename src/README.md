# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama 

```bash
# 1. Instalar Ollama (ollama.com)
#2. Baixar um modelo leve
ollama pull gpt-oss

#3. Testar se funciona
ollama run gpt-oss "Olá"

```


## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)

```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Código completo

Todo o código-fonte está no arquivo `app.py`.


## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py
```
## Evidências de execução
realizar um print da execução do Ollama



