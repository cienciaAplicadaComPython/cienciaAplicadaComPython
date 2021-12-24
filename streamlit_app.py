import streamlit as st
import time

'Começando um longo cálculo computacional...'

# Adiciona um marcador
ultima_iteracao = st.empty()
barra = st.progress(0)

for i in range(100):
  # Atualiza a barra de progresso a cada iteração
  ultima_iteracao.text(f'Iteração {i+1}')
  barra.progress(i + 1)
  time.sleep(0.1)

'...e agora está pronto!'
