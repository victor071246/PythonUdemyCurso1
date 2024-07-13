"""
Introdução ao desempacotamento + tuples (tuplas)
"""
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2)

_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)