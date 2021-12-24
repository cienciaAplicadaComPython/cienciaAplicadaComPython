import streamlit as st
import pandas as pd

st.write("A primeira tentativa para usar dados para criar uma tabela:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.table(df)
