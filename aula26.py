"""
Formatação básica de strings
s - string
d - int
f - float
.<numéro de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zero
Sinal + ou -
Ex.: 0> -100.1f 
Conversion flags - !r !s !a
__repr__
__str__
__ask__
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{variavel:$^10}')
print(f'{1000.251643513:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
