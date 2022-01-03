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


  ## O algoritmo
  
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
  
  
  ## Aperte o play!
  
  Simule o algoritmo descrito utilizando a linguagem de programação Python:


  """

conclusaoDoArtigo = """

  ## Conclusão
  
  
  Na prática, os valores das grandezas representados em diferentes unidades podem ser convertidos utilizando a seguinte fórmula
  
  $u_{final} = c \\times u_{original}$,
  
  na qual $u_{original}$ e $u_{final}$ são as medições da grandeza nas unidades original e final, respectivamente, e $c$ representa o coeficiente de conversão entre as unidas original e final, nesta ordem.
  
  Como exemplo, para convertermos $3$ m em pés devemos fazer $u_{pés} \\approx 3.2808 \\times 3 \implies u_{pés} \\approx 9,8425$ permitindo concluir que $3$ m equivalem aproximadamente a $9,8425$ pés.
  O uso do algoritmo implementado contribui para o cálculo quase instantâneo entre as conversões entre as unidades bastando informar o valor da medição e unidade original e a unidade final. O retrabalho de procurar os coeficientes de conversão sempre que deseja-se efetuar a conversão é evitado, uma vez que as tabelas utilizadas para a conversão permanecem salvas.

  """
