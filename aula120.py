# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios métodos e atributos.
# Os objetos gerados pelas classes podem usar seus dados internos para realizar várias ações
# Por conveção, usamos PascalCase para nomes de classes
# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string, str))  
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Otávio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)


