"""
Iterando strings com while
"""
#       0123456789
nome = 'Luiz Otávio' #Iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)

# print(nome[3])

# nova_string = '*L*u*i*z...'
nova_string = ''
contador = 0
while contador != len(nome): 
    nova_string += nome[contador] + '*'
    contador += 1
print(nova_string)