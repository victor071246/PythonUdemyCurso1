# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# a, b, *_, u = lista
# print(a, u)

# for nome in lista:
#     print(nome, end=' ')

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

print(*salas, sep='\n')