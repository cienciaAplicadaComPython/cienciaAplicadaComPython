import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Primeira coluna': [1, 2, 3, 4],
    'Segunda coluna': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Qual número você mais gosta?',
     df['Primeira coluna'])

'Você selecionou: ', option
