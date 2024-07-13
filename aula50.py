"""

Exercício
Exiba os indicadores da lista
0 Maria
1 Helena
2 Luiz
"""
# lista = ['Maria', 'Helena', 'Luiz']
# i = 0

# for nome in lista:
#     print(f'{i} {nome}')
#     i += 1
    
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))