import streamlit as st

coluna_esquerda, coluna_direita = st.columns(2)
# Você pode usar uma coluna como st.sidebar:
coluna_esquerda.button('Pressione-me!')

# Ou até melhor, chame funções Streamlit dentro de uma bloco "with":
with coluna_direita:
    chosen = st.radio(
        'Chapéu seletor',
        ("Grifinória", "Corvinal", "Lufa-lufa", "Sonserina"))
    st.write(f"Você está na casa {chosen}!")
