# Entendendo self em classes python
# Classe - Molde (geralmente sem dados)
# Instância de classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome):
        self.nome =  nome
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
Carro.acelerar()
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
# print(celta.nome)
# celta.acelerar()