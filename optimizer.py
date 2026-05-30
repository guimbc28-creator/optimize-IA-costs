import re

def otimizar_custo_contexto(texto_bruto: str) -> str:
    """
    Reduz o custo de tokens limpando a redundância sintática e estrutural 
    de textos longos antes do envio para a API de LLM.
    """
    # 1. Normaliza espaçamentos e quebras de linha repetidas (gargalo bobo de token)
    texto = re.sub(re.compile(r'\n+'), '\n', texto_bruto)
    texto = re.sub(re.compile(r' {2,}'), ' ', texto)
    
    # 2. Lista de stop-words e conectivos prolixos que incham o prompt sem adicionar semântica
    # (Em produção, pode ser expandido ou integrado a um tokenizador local)
    padroes_prolixos = {
        r'\b(por causa de que|com o objetivo de|no que diz respeito a)\b': 'para',
        r'\b(devido ao fato de que)\b': 'porque',
        r'\b(uma grande quantidade de)\b': 'vários',
        r'\b(com toda a certeza|obviamente)\b': 'certamente',
    }
    
    for padrao, substituto in padroes_prolixos.items():
        texto = re.sub(padrao, substituto, texto, flags=re.IGNORECASE)
        
    # 3. Remove redundâncias de palavras adjacentes idênticas (erros de digitação comuns em logs/transcrições)
    texto = re.sub(r'\b(\w+)( \1)+\b', r'\1', texto, flags=re.IGNORECASE)
    
    # 4. Mantém a estrutura essencial (instruções, dados, delimitadores) e poda o resto
    linhas_otimizadas = []
    for linha in texto.split('\n'):
        linha_limpa = linha.strip()
        if linha_limpa:
            # Filtra ruídos de formatação comuns que consomem bytes/tokens à toa
            linhas_otimizadas.append(linha_limpa)
            
    return '\n'.join(linhas_otimizadas)

# --- Exemplo de Impacto em Produção ---
prompt_prolixo = """
Prezado modelo de IA, eu gostaria que você, por causa de que precisamos analisar isso com urgência, 
fizesse a análise desse relatório. Devido ao fato de que o relatório possui uma grande quantidade de erros, 
foque principalmente nos bugs de memória.   memória.
"""

prompt_limpo = otimizar_custo_contexto(prompt_prolixo)
print(f"Antes: {len(prompt_prolixo.split())} palavras")
print(f"Depois: {len(prompt_limpo.split())} palavras")
print(f"\nResultado Pronto para API:\n{prompt_limpo}")