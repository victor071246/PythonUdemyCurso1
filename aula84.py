#List comprehension em Python
#List comprehension em Python é uma forma rápida para criar listas a partir de iteráveis
# print(list(range(10)))
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [numero * 2 for numero in range(10)]
# print(lista)

import pprint
# Mapeamento de dados em list comprehension
lista = []
produtos = [
    {'nome': 'p1', 'preco':20},
    {'nome': 'p2', 'preco':10},
    {'nome': 'p3', 'preco':30},
 ]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} #ternário
    for produto in produtos
]

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
pprint.pprint(novos_produtos)