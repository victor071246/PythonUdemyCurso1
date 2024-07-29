#List comprehension em Python
#List comprehension em Python é uma forma rápida para criar listas a partir de iteráveis
# print(list(range(10)))
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [numero * 2 for numero in range(10)]
# print(lista)

import pprint
def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)
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
    if (produto['preco'] >=  20 and produto['preco'] * 1.05 > 10)
]

# print(novos_produtos)
# lista = [n for n in range(10) if n < 5] 
p(novos_produtos)