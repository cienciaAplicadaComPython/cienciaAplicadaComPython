import streamlit as st

# Adiciona uma caixa de seleção ao menu lateral
add_selectbox = st.sidebar.selectbox(
    'Como você gostaria de ser contactado?',
    ('E-mail', 'Telefone residencial', 'Telefone móvel')
)

# Adicione um controle deslizante ao menu lateral:
add_slider = st.sidebar.slider(
    'Escolha um intervalo de valores',
    0.0, 100.0, (25.0, 75.0)
)
