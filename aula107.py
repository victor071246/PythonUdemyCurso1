# Exercício - Unir listas
# Crie uma função zipper (como zipper de roupas)
# O trabalho dessa função será unir duas listas em ordem
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [
#         (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#     ]

# zipper

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
# zipper(l1, l2)
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='(cidade não encontrada)')))