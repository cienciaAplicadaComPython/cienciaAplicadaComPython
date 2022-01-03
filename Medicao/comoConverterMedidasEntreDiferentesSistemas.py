textoDoArtigo = """
  
  # Como converter medidas entre sistemas diferentes?
  
  *Como converter as polegadas em metros ou vice-versa? O que a medida onças representa?
  Quais sistemas de medidas existem?
  Abaixo você encontra as respostas para todas essas perguntas.*
  
  Tempo de leitura: 5 minutos
  
  ---
  
  
  ## Introdução
  
  Realizamos medições quando queremos caracterizar um objeto, uma pessoa ou um animal por meio da comparação com padrões conhecidos de comprimento, massa, volume e outros.
  Podemos ainda avaliar o desempenho de atividades com o uso de padrões de velocidade, potências e outros.
  
  Os padrões internacionais são resultados de acordos entre cientistas de diferentes países sobre os procedimentos necessários para a reprodução destes padrões e eles são agrupados em **Sistemas de Medidas**. Atualmente, os seguintes sistemas de medidas são utilizados:
  - Sistema Internacional de Unidades (SI)
  - Sistema Imperial de Unidades
  
  
  ## O Sistema internacional de unidades
  
  Em 1971, na 14<sup>a</sup> Conferência Geral de Pesos e Medidas, sete grandezas foram selecionadas como fundamentais para constituir a base do SI:
  
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
  
  Este sistema foi primeiramente definido no ato britânico de 1824 de pesos e medidas e ele pode ser dividido em unidades de comprimento, área, volume e massa:
  
  |Nome da Unidade  |Símbolo da Unidade   |Equivalência com o SI          |
  |:--              |:--:                 |                            --:|              
  |                 |*Comprimento*        |                               |
  |Polegada         |in                   |0,0254 m                       |
  |Pés              |ft                   |0,3048 m                       |
  |Jardas           |yd                   |0,9144 m                       |
  |Milha            |mi                   |1.609,344 m                    |
  |                 |*Área*               |                               |
  |Acre             |mi                   |4.046,86 m<sup>2</sup>         |
  |Milha quadrada   |sq mi                |2.589.988,110336 m<sup>2</sup> |
  |                 |*Volume*             |                               |
  |Onças            |oz                   |0,0000295735 m<sup>3</sup>     |
  |Pinta            |pt                   |0,000473176 m<sup>3</sup>      |
  |Galão            |gal                  |0,00378541 m<sup>3</sup>       |
  |                 |*Massa*              |                               |
  |Libras           |lb                   |0,4536 kg                      |
  |Stones           |st                   |6,3503 kg                      |
  |Tonelada         |ton                  |1.016,0469 kg                  |


  ## O algoritmo
  
  Como base de um sistema com interfaceamento com o usuário, o algoritmo a ser utilizado deve requisitar os valores de cada um dos parâmetros de entrada.
  
  Os parâmetros de entrada devem ser:
  - A unidade original;
  - A unidade final para qual deseja-se realizar a conversão;
  - A medição realizada na unidade original.
  Com os valores dos parâmetros anteriores informados, a medição realizada para a unidade original deve ser convertida para a unidade final e retornada ao usuário.
  
  Para permitir que o usuário informe as unidades original e final e tenha o valor da medição convertido, a classe de tabelas de conversão é utilizada e caracterizada a seguir:
  - A única propriedade da classe indica quantas tabelas de conversão existem;
  - O único método da classe utiliza o valor da sua única propriedade para retornar uma tabela de conversão específica contendo as unidades aplicáveis para a grandeza em questão.
  
  Como adicional, o usuário deve ser instruído corretamente sobre os valores a serem informados e poder reexecutar o algoritmo o número de vezes desejado em sequência, informando quando não é mais necessário.

  """
