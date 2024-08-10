# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios métodos e atributos.
# Os objetos gerados pelas classes podem usar seus dados internos para realizar várias ações
# Por conveção, usamos PascalCase para nomes de classes
# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string, str))  
class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'

p2 = Pessoa()
p1.nome = 'Maria'
p1.sobrenome = 'Antonieta'


print(p1.nome)
print(p1.sobrenome)