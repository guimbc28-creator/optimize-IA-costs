# 📉 LLM Prompt Cost Optimizer

> "Porque eu sou 100% vibecoder, mas minha carteira não aguenta 100% do custo de tokens." ☕✨

Este é um helper simples e puramente algorítmico em Python feito para cortar o ruído de textos brutos (logs, transcrições, prompts prolixos) antes de enviá-los para APIs de LLM (como Gemini ou OpenAI).

## 🚀 Como funciona?
O script aplica filtros estritos de entropia sintática (via Regex convencional) para remover repetições, espaçamentos inúteis e conectivos vazios, reduzindo o payload de entrada em até 30% sem perder o contexto semântico.

## 🛠️ Como rodar
1. Clone o repositório
2. Configure sua chave da API: `export GEMINI_API_KEY="sua_chave_aqui"`
3. Execute o `optimizer.py`
