import streamlit as st

st.set_page_config(page_title='Ciência Aplicada com Python', page_icon = 'random')

topico = st.sidebar.radio(
    'Escolha um tópico:',
    (
        'Introdução',
        'Medição',
        'Mecânica'
    ),
)

if topico == 'Introdução':
         """
         # Intrdoução
         
         Está aplicação WEB contém uma coleção de artigos com respostas baseadas na ciência à perguntas feitas livremente.
         Muitas delas são inspiradas em leituras, filmes, séries, documentários e viagens.
         Cada artigo contém um algoritmo escrito com base na linguagem de programação *ython* que permite a utilização da solução proposta de maneira prática.
         
         Como objetivo, espera-se aumentar o interesse do leitor pela ciência, estimular a sua natureza investigativa e apoiar a integração entre a ciência e computação.
         
         *Obrigado por visitar **Ciência Aplicada com Python***
         """

st.caption('**Desenvolvido por**: Jefferson Silva')
st.caption('**E-mail**: j.davidss@hotmail.com')
