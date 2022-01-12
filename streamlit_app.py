import streamlit as st

st.set_page_config(page_title='Ciência Aplicada com Python na Web', page_icon = 'random')

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
         
    *Obrigado por visitar* ***Ciência Aplicada com Python na Web***.
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
        from Medicao.comoConverterMedidasEntreDiferentesSistemas import introducaoDoArtigo as introducaoDoArtigo
        from Medicao.comoConverterMedidasEntreDiferentesSistemas import codigoDeTabelaParaConversaoDeMedidas, parteFinalDoCodigoDoAlgoritmo, codigoPrincipalDoAlgoritmo, conclusaoDoAlgoritmo, conclusaoDoArtigo
        from Medicao.comoConverterMedidasEntreDiferentesSistemas import introducaoDoCodigoDoAlgoritmo as introducaoDoCodigoDoAlgoritmo
        
        introducaoDoArtigo 
        st.write('')
        introducaoDoCodigoDoAlgoritmo       
        st.code(codigoDeTabelaParaConversaoDeMedidas, language='python')
        parteFinalDoCodigoDoAlgoritmo
        st.code(codigoPrincipalDoAlgoritmo, language='python')
        conclusaoDoAlgoritmo
        st.write('')
        conclusaoDoArtigo
        st.write('')
        

elif topico == 'Mecânica':
    topicoDeMecanica = st.sidebar.radio(
        'Escolha um tópico de mecânica:',
        (
            'Quanto tempo demora uma ultrapassagem?',
            ""
        ),
    )
    
    if topicoDeMecanica == 'Quanto tempo demora uma ultrapassagem?':
        from Mecanica.quantoTempoDemoraUmaUltrapassagem import introducaoDoArtigo as introducaoDoArtigo
        from Mecanica.quantoTempoDemoraUmaUltrapassagem import imagemDeSituacaoInicial, continuacaoDaIntroducaoDoArtigo, conclusaoDaIntroducaoDoArtigo  
        
        introducaoDoArtigo
        st.image(imagemDeSituacaoInicial)
        imagemDeSituacaoInicial
        continuacaoDaIntroducaoDoArtigo 
        conclusaoDaIntroducaoDoArtigo 
        st.write('')

st.caption('**Desenvolvido por**: Jefferson Silva')
st.caption('**E-mail**: j.davidss@hotmail.com')
