"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""
contador = 0

while contador <= 10:
    contador += 1
    print(contador)

    if contador == 6:
        print(f'Não vou mostrar o {contador}')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar o {contador}')
        continue



print('Acabou')