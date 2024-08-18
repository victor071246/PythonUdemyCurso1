# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (nome)
# 3 - Crie uma classe Fabricante (nome)
# 4 Faça a ligação entre Carro possui Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exibe o nome do carro, motor e fabricantes na telas

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self._fabricante = None

        @property
        def motor(self):
            return self._motor
        
        @motor.setter
        def motor(self, valor):
            self._motor = valor

        @property
        def fabricante(self):
            return self._fabricante
        
        @fabricante.setter
        def fabricante(self, valor):
            self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0

uno = Carro('Uno')
fiat = Fabricante('Fiat')
uno.fabricante = fiat
uno.motor = motor_1_0

focus = Carro('Focus')
motor_1_0 = Motor('1.0')
ford = Fabricante('Ford')
focus.fabricante = ford
focus.motor = motor_1_0

print(f'{fusca.nome} | {fusca.fabricante.nome} | {fusca.motor.nome}')

