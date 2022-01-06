import streamlit as st

from Medicao.comoConverterMedidasEntreDiferentesSistemas import textoDoArtigo as textoDeComoConverterMedidasEntreDiferentesSistemas
from Medicao.codigoDoAlgoritmo import codigoDeTabelaParaConversaoDeMedidas as codigoDeTabelaParaConversaoDeMedidas
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
