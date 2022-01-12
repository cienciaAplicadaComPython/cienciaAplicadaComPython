introducaoDoArtigo = '''# Quanto tempo demora uma ultrapassagem?

*Sabe dizer quanto tempo você fica na pista contrária durante uma ultrapassagem?
Você poderia trazer grande risco a você mesmo e aos outros passageiros!
Entenda por meio deste exemplo de aplicação de física na vida real a dimensão desse risco.*

Tempo de leitura: 8 minutos

---

## Introdução

Se você já esteve na autoestrada, a manobra de ultrapassagem já se mostrou como uma alternativa para passar menos tempo nela.
Porém, essa é uma manobra que traz riscos e ter controle sobre ela reduz eles.
Se você souber dizer quanto tempo a ultrapassagem durará, você estará iniciando uma manobra com a vantagem de ter uma informação adicional sobre ela e isto fará você se sentir mais seguro.
Então vamos à resposta!

## Modelo

Recorreremos ao seguinte modelo para encontrar a resposta.

 - Dois veículos, $C_1$ e $C_2$, movem-se com velocidade constante na mesma direção e sentido, da esquerda para a direita.
 Chamemos este cenário de situação inicial.
 Os veículos $C_1$ e $C_2$ têm comprimento $d_{c_1}$ e $d_{c_2}$, respectivamente. A distância entre os veículos $C_1$ e $C_2$ é $d_{c_1c_2}$.'''

continuacaoDaIntroducaoDoArtigo = '''Após a ultrapassagem começar, vamos considerar que ela termina quando o veículo $C_1$ estiver à frente do veículo $C_2$ de uma distância igual a $d_{c_1c_2}$.
Chamemos este cenário de situação final:'''

conclusaoDaIntroducaoDoArtigo = '''Vamos desconsiderar o tempo que o carro leva para entrar na contramão, o atrito do asfalto, a resistência do vento e outras variáveis.

Assumindo então que os veículos movem-se em linha reta e com velocidade constante, da análise do movimento retilíneo uniforme temos a seguinte fórmula

$v = \\frac{d}{t}$

na qual $v$, $d$ e $t$ representam a velocidade, a distância e o tempo, respectivamente.
Aqui, vamos considerar somente a velocidade escalar.
Como desejamos encontrar o tempo durante o qual é realizada a ultrapassagem, ou seja $t$, e é necessário que o veículo $C_1$ esteja com uma velocidade superior ao do veículo $C_2$, vamos considerar a diferença entre as velocidades dos dois veículos, $\\Delta v$, ao invés de $v$.
Logo, para o veículo $C_1$ percorrrer uma distância de $d_{c_1c_2} + d_{c_2} + d_{c_1c_2} + d_{c_1}$ sendo que a sua velocidade é superior a velocidade do veículo $C_2$ por $\\Delta v$, será necessário um tempo de aproximadamente

$t = \\frac{d_{c_1} + d_{c_2} + 2 \\times d_{c_1c_2}}{\\Delta v}$

Ao utilizar a fórmula acima, sempre observe as unidades!
Caso você deseje utilizar $\\Delta v$ em km/h, será preciso converter os valores de distância para km. Neste caso, o resultado obtido para o tempo será em horas.
Para utilizar os valores comumente pensados na prática, ou seja, a diferença de velocidades em km/h e as distâncias em m e obter o tempo de ultrapassagem em s, podemos utilizar a seguinte equação:

$t = \\frac{\\frac{d_{c_1} + d_{c_2} + 2 \\times d_{c_1c_2}\; \\text{km}}{1000}}{\\Delta v\; \\text{km/h}} \\times \\frac{3.600\; \\text{s}}{\\text{h}} \\ t = \\frac{d_{c_1} + d_{c_2} + 2 \\times d_{c_1c_2}}{\\Delta v} \\times 3,6\; \\text{s}$.

## Modelo do Algoritmo

Como base de um sistema com interfaceamento com o usuário, o algoritmo a ser utilizado deve requisitar os valores de cada um dos parâmetros de entrada.
O modelo do sistema estabelece que os parâmetros de entrada devem ser:
 - O comprimento do veículo que realiza a manobra de ultrapassagem;
 - O comprimento do veículo a ser ultrapassado;
 - A distância entre os dois veículos;
 - A diferença entre as velocidades dos dois veículos.

Com os valores dos parâmetros anteriores informados, o tempo de duração deve ser calculado e retornado ao usuário.

Como adicional, o usuário deve poder reexecutar o algoritmo o número de vezes desejado em sequência, informando quando não é mais necessário.


## Colete os dados em campo

Na prática, os valores das grandezas da fórmula anterior podem ser coletados da seguinte maneira:
 - $d_{c_1}$ é o comprimento do seu veículo em **metros**.
 - $d_{c_2}$ é o comprimento do veículo a ser ultrapassado em **metros**. Observe:
   - Veículos longos apresentam o seu comprimento na traseira
   - A largura de um veículo varia em média entre 4 e 6,5 metros
 - $d_{c_1c_2}$ é a distância entre o seu veículo e o veículo a ser ultrapassado logo antes de começar a ultrapassagem em **metros**. Observe:
 - $\\Delta v$ é a diferença entre as velocidades do seu veículo quando esse está a uma distância $d_{c_1c_2}$ do veículo a ser ultrapassado e durante a ultrapassagem.'''

introducaoDoCodigoDoAlgoritmo = '''## Implemente o algoritmo

Simule o algoritmo a seguir utilizando a linguagem de programação Python.'''

codigoPrincipalDoAlgoritmo = '''import os

def clear(): 
 os.system('cls')

i = 0

while i == 0:
  
 print ('Calcula o tempo de ultrapassagem entre dois veiculos\\n')
 print('Informe os dados solicitados:\\n')
  
 dc1 = float(input('Comprimento do veiculo que realiza a ultrapassagem (em metros):\\n'))
 dc2 = float(input('Comprimento do veiculo a ser ultrapassado (em metros):\\n'))
 dc1c2 = float(input('A distancia entre os dois veiculos logo antes da ultrapassagem (em metros):\\n'))
 deltav = float(input('A diferenca entre as velocidades dos dois veiculos (em kilometros/hora):\\n'))
  
 t = (dc1 + dc2 + 2*dc1c2)/deltav*3.6
  
 print('O tempo de ultrapassagem calculado:\\n%.2f s' %t)
  
 i = int(input('\\nDeseja parar?\\nSim: 1\\nNao: 0\\n'))
  
  
 if i == 0:
  clear()'''

conclusaoDoAlgoritmo = '''**Execute o código e voilá!**'''

conclusaoDoArtigo = '''## Conclusão

Como exemplo, suponha os seguintes valores para as grandezas:
 - $d_{c_1} = 4$ m
 - $d_{c_2} = 20$ m
 - $d_{c_1c_2} = 100/3$ m
 - $v_i = 60$ km/h.

Realizando uma ultrapassagem com velocidade igual a $70$ km/h, teremos $\\Delta v = 10$ km/h.
Logo, o tempo de ultrapassagem será de 

$t = \\frac{4 + 20 + 2 \\times \\frac{100}{3}}{10} \\times 3,6\; \\text{s} \\ t = \\frac{816}{25}\; \\text{s} = 32,64\; \\text{s}$

O resultado revela que ultrapassar um veículo de $20$ m de comprimento movendo-se a uma velocidade igual a $60$ km/h com uma velocidade superior igual a $70$ km/h é extremamente perigoso, pois o tempo de ultrapassagem seria muito longo.
Se a velocidade de ultrapassagem for aumentada para $80$ km/h, o tempo de ultrapassagem será de

$t = \\frac{4 + 20 + 2 \\times \\frac{100}{3}}{20} \\times 3,6\; \\text{s} \\ t = \\frac{272}{60} \\times 3,6\; \\text{s} \\approx 16,32\; \\text{s}$

Agora entendemos que ultrapassar um veículo de $20$ m de comprimento movendo-se a uma velocidade igual a $60$ km/h com uma velocidade superior igual a $80$ km/h requer menos tempo.
No entanto, a ultrapassagem ainda custará um longo tempo antes de ser completada, o que a torna arriscada.
Nesse caso, é mais prudente realizar a ultrapassagem com uma velocidade superior a $80$ km/h.'''
