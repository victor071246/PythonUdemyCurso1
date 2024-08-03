# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - um problema que possa ser dividido em partes menores
# - um caso recursivo que resolve o pequeno problema
# - um caso base para a recursão
# - fatorial - n ! = 5 * 4 * 3 * 2 * 1 = 120
# import sys

# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)

#     # Caso base
#     if inicio >= fim:
#         return fim
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

def factorial(n):
    if n <= 1: 
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
print(factorial(100))