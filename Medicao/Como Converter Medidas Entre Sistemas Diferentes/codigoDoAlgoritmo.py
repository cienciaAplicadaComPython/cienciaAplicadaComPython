introducaoDoCodigoDoAlgoritmo = '''Crie a classe de tabelas de conversão em um arquivo *tabelaParaConversaoDeMedidas.py*:
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

codigoPrincipalDoAlgoritmo = '''
'''
