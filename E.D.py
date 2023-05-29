import statistics
import numpy as np
import scipy

class Calc:
    def __init__(self,dados):
        self.dados_tratado = sorted(dados)

    def mediana(self):
        valor = len(self.dados_tratado)

        if valor % 2 == 0:
            metade_d = valor//2
            metade_e = metade_d - 1
            mediana = (self.dados_tratado[metade_e] + self.dados_tratado[metade_d])/2
            resposta = (f'A mediana é: {mediana}')
        else:
            metade = valor//2
            mediana = self.dados_tratado[metade]
            resposta = (f'A mediana é: {mediana}')

        return resposta

    def media(self):
        calc = statistics.mean(self.dados_tratado)
        media = print(f'A média é de: {calc:.2f}')

        return media

    def moda(self):
        moda = statistics.multimode(self.dados_tratado)
        modar  = print(f'A moda da lista é: {moda}')

        return modar

    def valor_max(self):
        maior = max(self.dados_tratado)
        resposta = print(f'O maior valor na lista é {maior}')

        return  resposta

    def valor_min(self):
        menor = min(self.dados_tratado)
        resposta = print(f'O menor valor na lista é {menor}')

        return resposta

    def variancia(self):
        var = np.var(self.dados_tratado)
        resposta = print(f'A variância é de: {var:.2f}')

        return resposta

    def desvio_padrao(self):
        des = np.std(self.dados_tratado)
        resposta =print(f'O desvio padrão é de: {des:.2f}')

        return resposta

    def amplitude(self):
        maior = max(self.dados_tratado)
        menor = min(self.dados_tratado)
        amplitude = maior - menor

        resposta = print(f'A amplitude dessa lista é de: {amplitude}')

        return resposta

    def coeficiente_de_variacao(self):
        dp = statistics.stdev(self.dados_tratado)
        tamanho = len(self.dados_tratado)
        cv = (dp/tamanho)*100

        resposta = print(f'O coeficiente de variação é de: {cv:.2f}%')

        return resposta



# Aqui você coloca a sua lista, este é só um exemplo
lista = [15,15,15,15,20,30,300,40,40,50,10,2,1]

vl = Calc(lista)

vl.media()
vl.mediana()
vl.moda()
vl.variancia()
print()

vl.valor_max()
vl.valor_min()
print()

vl.amplitude()
vl.desvio_padrao()
vl.coeficiente_de_variacao()
print()