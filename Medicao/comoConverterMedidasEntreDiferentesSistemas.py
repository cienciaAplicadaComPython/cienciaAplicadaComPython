introducaoDoArtigo = """# Como converter medidas entre sistemas diferentes?
  
  *Como converter as polegadas em metros ou vice-versa? O que a medida onças representa?
  Quais sistemas de medidas existem?
  Abaixo você encontra as respostas para todas essas perguntas.*
  
  Tempo de leitura: 5 minutos
  
  ---
  
  
  ## Introdução
  
  Realizamos medições quando queremos caracterizar um objeto, uma pessoa ou um animal por meio da comparação com padrões conhecidos de comprimento, massa, volume e outros.
  Podemos ainda avaliar o desempenho de atividades com o uso de padrões de velocidade, potências e outros.
  
  Os padrões internacionais são resultados de acordos entre cientistas de diferentes países sobre os procedimentos necessários para a reprodução desses padrões e eles são agrupados em **Sistemas de Medidas**. Atualmente, os seguintes sistemas de medidas são utilizados:
  - Sistema Internacional de Unidades (SI)
  - Sistema Imperial de Unidades
  
  
  ## O sistema internacional de unidades
  
  Em $1971$, na $14^a$ Conferência Geral de Pesos e Medidas, sete grandezas foram selecionadas como fundamentais para constituir a base do SI:
  
  |Grandeza                 |Nome da Unidade    |Símbolo da Unidade   |
  |:--                      |:--:               |                  --:|
  |Comprimento              |metro              |m                    |
  |Massa                    |kilograma          |kg                   |
  |Tempo                    |segundo            |s                    |
  |Temperatura              |kelvin             |K                    |
  |Quantidade de substância |mol                |mol                  |
  |Densidade luminosa       |candela            |Cd                   |
  |Corrente elétrica        |ampere             |A                    |

  Outras unidades são derivadas das unidades fundamentais do SI. Por exemplo, a grandeza força é representada pela unidade newton (N) a qual equivale a kg*.*m/s.
  
  
  ## O sistema imperial de unidades
  
  Este sistema foi primeiramente definido no ato britânico de $1824$ de pesos e medidas e ele pode ser dividido em unidades de comprimento, área, volume e massa:
  
  |Nome da Unidade  |Símbolo da Unidade   |Equivalência com o SI          |
  |:--              |:--:                 |                            --:|              
  |                 |*Comprimento*        |                               |
  |Polegada         |in                   |$0,0254$ m                     |
  |Pés              |ft                   |$0,3048$ m                     |
  |Jardas           |yd                   |$0,9144$ m                     |
  |Milha            |mi                   |$1.609,344$ m                  |
  |                 |*Área*               |                               |
  |Acre             |ac                   |$4.046,86$ m$^{2}$             |
  |Milha quadrada   |sq mi                |$2.589.988,110336$ m$^2$       |
  |                 |*Volume*             |                               |
  |Onças            |oz                   |$0,0000295735$ m$^3$           |
  |Pinta            |pt                   |$0,000473176$ m$^3$             |
  |Galão            |gal                  |$0,00378541$ m$^3$              |
  |                 |*Massa*              |                               |
  |Libras           |lb                   |$0,4536$ kg                    |
  |Stones           |st                   |$6,3503$ kg                    |
  |Tonelada         |ton                  |$1.016,0469$ kg                |


  ## Modelo do algoritmo
  
  Como base de um sistema com interfaceamento com o usuário, o algoritmo a ser utilizado deve requisitar os valores de cada um dos parâmetros de entrada.
  
  Os parâmetros de entrada devem ser:
  - A unidade original;
  - A unidade final para qual deseja-se realizar a conversão;
  - A medição realizada na unidade original.
  
  Com os valores dos parâmetros anteriores informados, a medição realizada para a unidade original deve ser convertida para a unidade final e retornada ao usuário.
  
  Para permitir que o usuário informe as unidades original e final e tenha o valor da medição convertido, uma classe de tabelas de conversão como caracterizada a seguir é utilizada:
  - A única propriedade da classe indica quantas tabelas de conversão existem;
  - O único método da classe utiliza o valor da sua única propriedade para retornar uma tabela de conversão específica contendo as unidades aplicáveis para a grandeza em questão.
  
  Como adicional, o usuário deve ser instruído corretamente sobre os valores a serem informados.

  
  ## Colete os dados em campo
  
  Para a criação das tabelas de conversão entre as unidades, pode-se consultar fontes externas contendo constantes de conversão já calculadas.
  
  Caso deseje-se utilizar grandezas inventadas, um bom exercício é inspirar-se no Sistema Imperial de Unidades e utilizar as partes do corpo de um indivíduo ou de um objeto.
  Por exemplo, os braços, mãos e pernas de uma pessoa ou as pernas e assento de uma cadeira.
  """

introducaoDoCodigoDoAlgoritmo = '''## Implemente o algoritmo!

  Crie a classe de tabelas de conversão em um arquivo *tabelaParaConversaoDeMedidas.py*:'''

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

parteFinalDoCodigoDoAlgoritmo = '''Implemente o código que instancia uma tabela de conversão da classe e realiza a conversão entre as medições:'''

codigoPrincipalDoAlgoritmo = '''# Importa os modulos necessarios
import os 
from  tabelaParaConversaoDeMedidas import tabelaParaConversaoDeMedidas

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
        clear()'''

conclusaoDoArtigo = """## Conclusão
  
  
  Na prática, os valores das grandezas representados em diferentes unidades podem ser convertidos utilizando a seguinte fórmula
  
  $u_{final} = c \\times u_{original}$,
  
  na qual $u_{original}$ e $u_{final}$ são as medições da grandeza nas unidades original e final, respectivamente, e $c$ representa o coeficiente de conversão entre as unidas original e final, nesta ordem.
  
  Como exemplo, para convertermos $3$ m em pés devemos fazer $u_{pés} = c \\times u_{metros} \implies u_{pés} \\approx 3 \\times 3.2808 \implies u_{pés} \\approx 9,8425$ permitindo concluir que $3$ m equivalem aproximadamente a $9,8425$ pés.
  
  O uso do algoritmo implementado contribui para o cálculo quase instantâneo entre as conversões entre as unidades bastando informar o valor da medição e unidade original e a unidade final. O retrabalho de procurar os coeficientes de conversão sempre que deseja-se efetuar a conversão é evitado, uma vez que as tabelas utilizadas para a conversão permanecem salvas."""
