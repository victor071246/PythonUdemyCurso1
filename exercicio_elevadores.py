respostas_possiveis = ['A', 'B', 'C']
A_quantidade_uso = 0
B_quantidade_uso = 0
C_quantidade_uso = 0



moradores =  int(input('Insira a quantidade de moradores que farão a pesquisa: '))
for morador in moradores:
    flag = False
    elevador_usado = input('Entre A, B e C, qual o elevador que você mais utiliza?')
    if elevador_usado in respostas_possiveis:
        if elevador_usado == 'A':
            A_quantidade_uso += 1
    
    
    