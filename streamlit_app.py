import streamlit as st
import os

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
        Crie a classe de tabelas de conversão:
        '''
        with st.echo():          
            # Classe com todas as tabelas de conversao
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
                  ["5      ", "       ", "st     ", "6.35041", "14     ", "1      "]]
        
        '''
        Implemente o código que instância uma tabela de conversão da classe e realiza a conversão entre as medições:
        '''
        with st.echo():
            # Funcao para limpar a tela
            def clear(): 
              os.system('cls')

            # Valor inicial de variavel de controle
            desejaCont = 1

            # Instancia a classe com todas as tabelas para conversao de medidas
            instanciaDoObjetoComTodasAsTabelas = tabelaParaConversaoDeMedidas()

            while desejaCont: #enquanto deseja continuar
              # Valores iniciais de variaveis de controle
              posInicSetaEsquer = 3
              posInicSetaAcima = 3

              # Solicita escolher para qual grandeza sera feita a conversao
              erroGrandezaEscolh = True
              while erroGrandezaEscolh:
                print("Digite o numero correspondente a grandeza para a qual voce deseja realizar uma conversao de unidades:")
                grandezaEscolhida = int(input("1: Comprimento\n2: Massa\n"))
                if grandezaEscolhida in range(1, instanciaDoObjetoComTodasAsTabelas.qtdDeTabelas + 1):
                  erroGrandezaEscolh = False
                  tabelaConversao = instanciaDoObjetoComTodasAsTabelas.gerarTabela(grandezaEscolhida)
                else:
                  print("\u001b[31mErro: O numero correspondente a grandeza nao pode ser diferente de:")
                  for i in range(1, instanciaDoObjetoComTodasAsTabelas.qtdDeTabelas + 1):
                    print(i)
                  print ("\033[0;0m")

              # Imprime a tabela para conversao de unidades correspondente a grandeza escolhida
              print("A tabela correspondente para conversao de unidades e:")
              opcaoConversaoCorreta = 0
              while opcaoConversaoCorreta == 0: #enquanto o usuario nao confirmar a posicao de linhas e colunas
                valorAceitPosColunMovSetaAcima = []
                valorAceitPosLinhaMovSetaEsquer = []
                for i in range(0, len(tabelaConversao)):
                  print(" ".join(tabelaConversao[i]))
                  if i == 0: #armazena
                    for j in range(3,len(tabelaConversao[i])): #a quantidade aceita
                      valorAceitPosColunMovSetaAcima.append(tabelaConversao[i][j].strip()) #de colunas
                  if i > 2: #armazena a quantidade aceita
                    valorAceitPosLinhaMovSetaEsquer.append(tabelaConversao[i][0].strip()) #de linhas

                # Solicita escolher a posicao de linha
                erroQtdLinhas = True
                print("\n")
                while erroQtdLinhas:
                  movSetaEsquer = input("Digite a posicao de linha para mover a seta ao lado esquerdo:\n")
                  movSetaEsquerValid = False
                  for i in valorAceitPosLinhaMovSetaEsquer:
                    if movSetaEsquer == i:
                      movSetaEsquerValid = True
                      break
                  if movSetaEsquerValid:
                    erroQtdLinhas = False
                  else:
                    print("\u001b[31mErro: A posicao de linha nao pode ser diferente de:")
                    for i in valorAceitPosLinhaMovSetaEsquer:
                      print(i)
                    print ("\033[0;0m")
                tabelaConversao[posInicSetaEsquer][1] = len(tabelaConversao[posInicSetaEsquer][2])*" "
                tabelaConversao[int(movSetaEsquer)][1] = ">" + (len(tabelaConversao[posInicSetaEsquer][2]) - 1)*" "
                posInicSetaEsquer = int(movSetaEsquer)

                # Solicita escolher a posicao de coluna
                erroQtdColun = True
                print("\n")
                while erroQtdColun:
                  movSetaAcim = input("Digite a posicao de coluna para mover a seta acima:\n")
                  movSetaAcimValid = False
                  for i in valorAceitPosColunMovSetaAcima:
                    if movSetaAcim == i:
                      movSetaAcimValid = True
                      break
                  if movSetaAcimValid:
                    erroQtdColun = False
                  else:
                    print("\u001b[31mErro: A posicao de coluna nao pode ser diferente de:")
                    for i in valorAceitPosColunMovSetaAcima:
                      print(i)
                    print ("\033[0;0m")
                tabelaConversao[1][posInicSetaAcima] = len(tabelaConversao[2][posInicSetaAcima])*" "
                tabelaConversao[1][int(movSetaAcim)] = "v" + (len(tabelaConversao[2][posInicSetaAcima]) - 1)*" "
                posInicSetaAcima = int(movSetaAcim)

                # Limpa a tela
                clear()

                # Imprime a tabela com as setas nas posicoes de linha e coluna selecionadas
                for i in range(0, len(tabelaConversao)):
                  print(" ".join(tabelaConversao[i]))

                # Solicita confirmacao
                print("\nVoce deseja converter medidas de %s para %s" %(tabelaConversao[int(movSetaEsquer)][2].strip(), tabelaConversao[2][int(movSetaAcim)].strip()))
                opcaoConversaoCorreta = int(input("Correto?\n0: Nao\n1: Sim\n"))

                # Limpa a tela caso as posicoes de linha e coluna devam ser escolhidas novamente
                if opcaoConversaoCorreta == 0:
                  clear()

              # Solicita o valor da medicao original    
              medicaoOrig = input("Digite o valor da medicao em %s\n" %tabelaConversao[int(movSetaEsquer)][2].strip())

              # Calcula o valor da medicao final
              medicaoFinal = float(medicaoOrig)*float(tabelaConversao[int(movSetaEsquer)][int(movSetaAcim)])

              # Imprime o valor da medicao final calculado
              print("A medicao %s %s equivale a %s %s" %(medicaoOrig, tabelaConversao[int(movSetaEsquer)][2].strip(), medicaoFinal, tabelaConversao[2][int(movSetaAcim)].strip()))

              # Solicita confirmar se deseja continuar    
              desejaCont = int(input("\nVoce deseja continuar?\n0: Nao\n1: Sim\n"))

              if desejaCont == 1:
                clear()
        
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
