primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if(primeiro_valor > segundo_valor):
    print(f'O primeiro, {primeiro_valor} valor é maior que o segundo valor, {segundo_valor}')
elif(primeiro_valor < segundo_valor):
    print(f'O segundo valor, {segundo_valor} é maior que o primeiro valor, {primeiro_valor}')
else:
    print('Os valores são iguais')