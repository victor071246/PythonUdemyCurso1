nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / (altura ** 2)
# F strings
linha_1 = f'{nome} tem {altura: .2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é: {imc}'

print(linha_1)
print(linha_2)
print(imc)

# Luiz otávio tem 1.80 de altura,
# pesa 95 quilos e seu imc é
# 29.32098