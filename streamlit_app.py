import streamlit as st

from Medicao.comoConverterMedidasEntreDiferentesSistemas import textoDoArtigo as textoDeComoConverterMedidasEntreDiferentesSistemas
from Medicao.comoConverterMedidasEntreDiferentesSistemas import conclusaoDoArtigo as conclusaoDeComoConverterMedidasEntreDiferentesSistemas

st.set_page_config(page_title='Ciência Aplicada com Python', page_icon = 'random')

topico = st.sidebar.selectbox(
    'Escolha um tópico:',
    (
        'Introdução',
        'Medição',
        'Mecânica'
    ),
)

if topico == 'Introdução':
    """
    # Introdução
         
    Está aplicação WEB contém uma coleção de artigos com respostas baseadas na ciência à perguntas feitas livremente.
    Muitas delas são inspiradas em leituras, filmes, séries, documentários e viagens.
    
    Cada artigo contém um algoritmo escrito com base na linguagem de programação *Python* que permite a utilização da solução proposta de maneira prática.
         
    Como objetivo, espera-se aumentar o interesse do leitor pela ciência, estimular a sua natureza investigativa e apoiar a integração entre a ciência e computação.
    
    Para baixar e instalar a última versão de Python, acesse [Python Org](https://www.python.org/downloads/).
         
    *Obrigado por visitar* ***Ciência Aplicada com Python***
    """
        
elif topico == 'Medição':
    topicoDeMedicao = st.sidebar.radio(
        'Escolha um tópico de medição:',
        (
            'Como converter medidas entre sistemas diferentes?',
            ""
        ),
    )
    
    if topicoDeMedicao == 'Como converter medidas entre sistemas diferentes?':
        textoDeComoConverterMedidasEntreDiferentesSistemas
        st.write('')
        
        '''
        Crie a classe de tabelas de conversão em um arquivo *tabelaParaConversaoDeMedidas.py*:
        '''
        codigoDeTabelaParaConversaoDeMedidas = '''# Classe com todas as tabelas de conversao
class tabelaParaConversaoDeMedidas:
    def __init__(self):
        self.qtdDeTabelas = 2 #propriedade para armazenar o numero de tabelas

    def gerarTabela(self, grandezaEscolhida): #retorna a tabela de conversao para a grandeza escolhida
        if grandezaEscolhida == 1:
            return [["       ", "       ", "       ", "3      ", "4      ", "5      ", "6      ", "7      "],
            ["       ", "       ", "       ", "v      ", "       ", "       ", "       ", "       "],
            ["       ", "       ", "       ", "m      ", "in     ", "ft     ", "yd     ", "mi     "],
            ["3      ", ">      ", "m      ", "1      ", "39.3701", "3.2808 ", "1.0936 ", "0.0006 "],
            ["4      ", "       ", "in     ", "0.0254 ", "1      ", "0.08333", "0.02778", "0.00002"],
            ["5      ", "       ", "ft     ", "0.3048 ", "12.0005", "1      ", "0.33333", "0.00019"],
            ["6      ", "       ", "yd     ", "0.9144 ", "35.9971", "3      ", "1      ", "0.00057"],
            ["7      ", "       ", "mi     ", "1609.34", "50000  ", "5623.16", "1754.38", "1      "]]

         elif grandezaEscolhida == 2:
            return [["       ", "       ", "       ", "3      ", "4      ", "5      "],
            ["       ", "       ", "       ", "v      ", "       ", "       "],
            ["       ", "       ", "       ", "kg     ", "lbs    ", "st     "],
            ["3      ", ">      ", "kg     ", "1      ", "2.20462", "0.15747"],
            ["4      ", "       ", "lbs    ", "0.45359", "1      ", "0.07143"],
            ["5      ", "       ", "st     ", "6.35041", "14     ", "1      "]]'''
        st.code(codigoDeTabelaParaConversaoDeMedidas, language='python')
        
        '''
        Implemente o código que instancia uma tabela de conversão da classe e realiza a conversão entre as medições:
        '''
        codigoPrincipal = '''def hello():
            print("Hello, Streamlit!")'''
        st.code(codigoPrincipal, language='python')
            
        conclusaoDeComoConverterMedidasEntreDiferentesSistemas
        st.write('')
        

elif topico == 'Mecânica':
    topicoDeMecanica = st.sidebar.radio(
        'Escolha um tópico de mecânica:',
        (
            'Como converter medidas?',
            ""
        ),
    )
    
    if topicoDeMecanica == 'Como converter medidas?':
        """
        # Em desenvolvimento
        """

st.caption('**Desenvolvido por**: Jefferson Silva')
st.caption('**E-mail**: j.davidss@hotmail.com')
