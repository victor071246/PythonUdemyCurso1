"""
Introdução às funções (def) em python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornan None (nada)
"""

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Usuário'):
    print(f'Olá {nome}')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')


