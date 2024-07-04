import sys
"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digitar um número inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input('Digite um número inteiro')

try:
    numero_inteiro_int = int(numero_inteiro)
    if numero_inteiro_int % 2 == 0:
        print('O número escolhido é par')
    else:
        print('O número escolhido é ímpar')
except:
    print('Você não digitou um número')

"""
Faça um programa que pergunte o horário ao usuário e baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
horario_str = input('Digite o horário atual em horas: ')
try:
    horario = int(horario_str)
    if horario >= 0 and horario < 12:
        print('Bom dia!')
    elif horario > 12 and horario < 18:
        print('Boa tarde')
    elif horario > 18 and horario <=23:
        print('Boa noite!')
    else:
        print('Você não escolheu um horário válido, digite uma hora de 0 a 24')
except:
    print('Você não escolheu um horário válido, digite uma hora de 0 a 24')

"""
Faça um programa que peça o nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite seu nome: ')
caracteres_nao_permitidos= '0123456789_-+@!#$%¨&*()[]'
condicao_parada = False
for caractere in caracteres_nao_permitidos:
    if caractere in nome:
        condicao_parada = True
if condicao_parada == True:
    print('O nome não pode conter números ou caracteres especiais')
    sys.exit(0)
        
if nome:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) > 4 and len(nome) < 7:
        print('Seu nome é normal')
    else:
        print('Seu nome é longo')
else: print('Você não inseriu nada')