# # # Dicionários em Python (tipo dict)
# # # Dicionários são estruturas do tipo par de 'chave' e 'valor'.
# # # Chaves podem ser consideradas como o 'índice' que vimos nas listas e são de tipo imutável, como str, int, float, bool, tuple, etc.
# # # O valor pode ser de qualquer tipo, incluindo outro dicionário.
# # # Usamos as chaves - {} - ou a classe dict para criar dicionários.
# # # Imutáveis: str, int, float, bool, tuple.
# # # Mutáveis: dict, list
# # # pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# # # pessoa = {
# # #     'nome': 'Luiz Otávio',
# # #     'sobrenome': 'Miranda',
# # # }
# # pessoa = {
# #     'nome': 'Luiz Otávio',
# #     'sobrenome': 'Miranda',
# #     'idade': 18,
# #     'altura': 1.8,
# #     'endereços': [
# #         {'rua': 'tal tal', 'número': 123},
# #         {'rua': 'outra rua', 'número': 321}
# #     ]
# # }
# # # print(pessoa, type(pessoa))
# # print(pessoa['nome'])
# # print(pessoa['sobrenome'])

# # for chave in pessoa:
# #     print(chave, pessoa[chave])

# # Manipulando chaves e valores em dicionários
# pessoa = {}

# ##
# ##

# chave = 'nome'

# pessoa [chave] = 'Luiz Otávio'
# pessoa ['sobrenome'] = 'Miranda'
# lista = []

# print(pessoa[chave])

# pessoa[chave] = 'Maria'

# del pessoa ['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])

# # print('Isso não vai')


"""
Métodos úteis dos dicionários em Python
# len        - quantas chaves
# keys       - iterável com as chaves
# values     - iterável com os valores
# items      - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy       - retorna uma cópia rasa (shallow copy)
# get        - obtém uma chave
# pop        - apaga um item com uma chave especificada (del)
# popitem    - apaga o último item adicionado
# update     - atualiza um dicionário com o outro
"""
# pessoa.setdefault('idade', None)
# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values:
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
# import copy
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# # d2 = copy.copy(d1)
# d2 = d1.copy()

# d2['c1'] = 1000
# d2['c1']= 99999
# print(d1)
# print(d2)
p1 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade' : 900,  
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.popitem('nome')
# print(nome)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade':30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome'), ('novo valor'))
lista = [['nome'], ['novo valor']]
p1.update(lista)
print(p1)