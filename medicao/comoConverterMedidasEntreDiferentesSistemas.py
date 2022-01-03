        <article id="page_text">
            <header>
                <h1>Como converter medidas entre sistemas diferentes?</h1> 
                <p>
                    <em>
                        Como converter as polegadas em metros ou vice-versa? O que a medida onças representa? Quais sistemas de medidas existem?
                        Abaixo você encontra as respostas para todas essas perguntas.
                    </em>
                </p>
                <p>
                    Tempo de leitura: 5 minutos
                </p>
                
                <hr>
                
            </header>
            <section>
                <h3>Introdução</h3> 
                <p>
                   Realizamos medições quando queremos caracterizar um objeto, uma pessoa ou um animal por meio da comparação com padrões conhecidos de comprimento, massa, volume e outros.
                   Podemos ainda avaliar o desempenho de atividades com o uso de padrões de velocidade, potências e outros.
                </p>
                <p>
                   Os padrões internacionais são resultados de acordos entre cientistas de diferentes países sobre os procedimentos necessários para a reprodução destes padrões e eles são agrupados em <b>Sistemas de Medidas</b>.
                   Atualmente, os seguintes sistemas de medidas são utilizados:
                </p>
                <ul>
                    <li>Sistema Internacional de Unidades (SI)</li>
                    <li>Sistema Imperial de Unidades</li>
                </ul>
            </section>
            <section>
                <h3>O Sistema internacional de unidades</h3> 
                <p>
                    Em 1971, na 14<sup>a</sup> Conferência Geral de Pesos e Medidas, sete grandezas foram selecionadas como fundamentais para constituir a base do SI:
                </p>
                <table>
                    <caption>Sistema Internacional de Unidades</caption>
                    <tr>
                        <th>Grandeza</th>
                        <th>Nome da Unidade</th>
                        <th>Símbolo da Unidade</th>
                    </tr>
                    <tr>
                        <td>Comprimento</td>
                        <td>metro</td>
                        <td>m</td>
                    </tr>
                    <tr>
                        <td>Massa</td>
                        <td>kilograma</td>
                        <td>kg</td>
                    </tr>
                    <tr>
                        <td>Tempo</td>
                        <td>segundo</td>
                        <td>s</td>
                    </tr>
                    <tr>
                        <td>Temperatura</td>
                        <td>kelvin</td>
                        <td>K</td>
                    </tr>
                    <tr>
                        <td>Quantidade de substância</td>
                        <td>mol</td>
                        <td>mol</td>
                    </tr>
                    <tr>
                        <td>Densidade luminosa</td>
                        <td>candela</td>
                        <td>Cd</td>
                    </tr>
                    <tr>
                        <td>Corrente elétrica</td>
                        <td>ampere</td>
                        <td>A</td>
                    </tr>
                </table>
                <p>
                    Outras unidades são derivadas das unidades fundamentais do SI.
                    Por exemplo, a grandeza força é representada pela unidade newton (N) a qual equivale a kg$\times$m/s.
                </p>
            </section>
            <section>
                <h3>O sistema imperial de unidades</h3>
                <p>
                    Este sistema foi primeiramente definido no ato britânico de 1824 de pesos e medidas e ele pode ser dividido em unidades de comprimento, área, volume e massa:
                </p>
                <table>
                    <caption>Sistema Imperial de Unidades</caption>
                    <tr>
                        <th>Nome da Unidade</th>
                        <th>Símbolo da Unidade</th>
                        <th>Equivalência com o SI</th>
                    </tr>
                    <tr>
                        <td colspan = '3' style = 'text-align: center;'>Comprimento</td>
                    </tr>
                    <tr>
                        <td>Polegada</td>
                        <td>in</td>
                        <td>$0,0254$ m</td>
                    </tr>
                    <tr>
                        <td>Pés</td>
                        <td>ft</td>
                        <td>$0,3048$ m</td>
                    </tr>
                    <tr>
                        <td>Jardas</td>
                        <td>yd</td>
                        <td>$0,9144$ m</td>
                    </tr>
                    <tr>
                        <td>Milha</td>
                        <td>mi</td>
                        <td>$1.609,344$ m</td>
                    </tr>
                    <tr>
                        <td colspan = '3' style = 'text-align: center;'>Área</td>
                    </tr>
                    <tr>
                        <td>Acre</td>
                        <td>mi</td>
                        <td>$4.046,86$ m<sup>2</sup></td>
                    </tr>
                    <tr>
                        <td>Milha quadrada</td>
                        <td>sq mi</td>
                        <td>$2.589.988,110336$ m<sup>2</sup></td>
                    </tr>
                    <tr>
                        <td colspan = '3' style = 'text-align: center;'>Volume</td>
                    </tr>
                    <tr>
                        <td>Onças</td>
                        <td>oz</td>
                        <td>$0,0000295735$ m<sup>3</sup></td>
                    </tr>
                    <tr>
                        <td>Pinta</td>
                        <td>pt</td>
                        <td>$0,000473176$ m<sup>3</sup></td>
                    </tr>
                    <tr>
                        <td>Galão</td>
                        <td>gal</td>
                        <td>$0,00378541$ m<sup>3</sup></td>
                    </tr>
                    <tr>
                        <td colspan = '3' style = 'text-align: center;'>Massa</td>
                    </tr>
                    <tr>
                        <td>Libras</td>
                        <td>lb</td>
                        <td>$0,4536$ kg</td>
                    </tr>
                    <tr>
                        <td>Stones</td>
                        <td>st</td>
                        <td>$6,3503$ kg</td>
                    </tr>
                    <tr>
                        <td>Tonelada</td>
                        <td>ton</td>
                        <td>$1.016,0469$ kg</td>
                    </tr>
                </table>
            </section>
            <section id = "algoritmo_section">
                <h3>O algoritmo</h3>
                <p>Como base de um sistema com interfaceamento com o usuário, o algoritmo a ser utilizado deve requisitar os valores de cada um dos parâmetros de entrada.</p>
                <p>O modelo do sistema estabelece que os parâmetros de entrada devem ser:</p>
                <ul>
                    <li>A unidade original;</li>
                    <li>A unidade final para qual deseja-se realizar a conversão;</li>
                    <li>A medição realizada na unidade original.</li>
                </ul>
                <p>Com os valores dos parâmetros anteriores informados, a medição realizada para a unidade original deve ser convertida para a unidade final e retornada ao usuário.</p>
                <p>Para permitir que o usuário informe as unidades original e final e tenha o valor da medição convertido, a classe de tabelas de conversão é utilizada e caracterizada a seguir:</p>
                <ul>
                    <li>A única propriedade da classe indica quantas tabelas de conversão existem;</li>
                    <li>O único método da classe utiliza o valor da sua única propriedade para retornar uma tabela de conversão específica contendo as unidades aplicáveis para a grandeza em questão.</li>
                </ul>
                <p>Como adicional, o usuário deve ser instruído corretamente sobre os valores a serem informados e poder reexecutar o algoritmo o número de vezes desejado em sequência, informando quando não é mais necessário.</p>
            </section>
            <section id = "colete_dados_em_campo_section">
                <h3>Colete os dados em campo</h3>
                <p>Para a criação das tabelas de conversão entre as unidades, pode-se consultar fontes externas contendo constantes de conversão já calculadas.</p>
                <p>Caso deseje-se utilizar grandezas inventadas, um bom exercício é inspirar-se no Sistema Imperial de Unidades e utilizar as partes do corpo de um indivíduo ou de um objeto.
                    Por exemplo, os braços, mãos e pernas de uma pessoa ou as pernas e assento de uma cadeira.
                </p>
            </section>
            <section id = "aperte_o_play_section">
                <h3>Aperte o play!</h3>
                <p>Simule o algoritmo descrito utilizando a linguagem de programação Python:</p>
                <iframe src="https://trinket.io/embed/python/9f53c26070" width = 99.5% height = 600em frameborder = 10em marginwidth = 0em marginheight = 0em allowfullscreen title = "Algoritmo em Python"></iframe>
            </section>
            <section id = "conclusao_section">
                <h3>Conclusão</h3>
                <p>
                    Na prática, os valores das grandezas representados em diferentes unidades podem ser convertidos utilizando a seguinte fórmula
                    $$u_\text{final} = c \times u_\text{original},$$
                    na qual $u_\text{original}$ e $u_\text{final}$ são as medições da grandeza nas unidades original e final, respectivamente, e $c$ representa o coeficiente de conversão entre as unidas original e final, nesta ordem.
                </p>
                <p>
                    Como exemplo, para convertermos $3$ m em pés devemos fazer
                    $$u_\text{pés} \approx 3.2808 \times 3 \implies u_\text{pés} \approx 9,8425$$
                    permitindo concluir que $3$ m equivalem aproximadamente a $9,8425$ pés.
                </p>
                <p>
                    O uso do algoritmo implementado contribui para o cálculo quase instantâneo entre as conversões entre as unidades bastando informar o valor da medição e unidade original e a unidade final.
                    O retrabalho de procurar os coeficientes de conversão sempre que deseja-se efetuar a conversão é evitado, uma vez que as tabelas utilizadas para a conversão permanecem salvas.
                </p>
            </section>
        </article>  
