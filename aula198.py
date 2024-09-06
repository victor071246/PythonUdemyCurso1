# Deque - Trabalhando com LIFO e FIFO
# deque - Double-ended queue
# Lifo e Fifo
# Pilha e Fila

# LIFO (Last In First Out)
# Pilha (stack)
# Siginifica que o último item a entrar será o último item a sair (list)
# Artigo:
# https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack;
# Vídeo:
# https://youtube.be/svWVHEihyNI
# Para tirar itens do final: O(1) Tempo constate
# Para tirar itens do início: O(n) Tempo linear

from collections import deque
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Legal (LIFO com lista)
lista.append(10)

lista.append(11)

ultimo_removido = lista.pop()

print('Último: ', ultimo_removido)
print('Lista: ',lista)
# ------------------------------------------------------------ 

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ruim (FIFO com lista)
lista.insert(0, 10)

lista.insert(0, 11)

primeiro_removido = lista.pop(0)

print('Primeiro: ', primeiro_removido)
print('Lista: ', lista)
print()

# Legal (FIFO com deque)

fila_correta: deque[int] = deque()
fila_correta.append(3) # Adiciona no final
fila_correta.append(4) # Adiciona no final
fila_correta.append(5) # Adiciona no final
fila_correta.appendleft(0) # Adiciona no começo
fila_correta.appendleft(1) # Adiciona no começo
fila_correta.appendleft(2) # Adiciona no começo
print(fila_correta) # deque([2, 1, 0, 3, 4, 5])
fila_correta.pop() #5
fila_correta.popleft() # 2
print(fila_correta) # deque [1, 0, 3, 4]