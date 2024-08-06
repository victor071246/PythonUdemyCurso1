# Exercício - Lista de tarefas com desfazer e refazer
# Música pra codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar ']
import os
tarefas = []
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar\n')
        return
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'{tarefa}\n')

def adicionar():
    print()
    tarefa = input('Digite a tarefa que deseja adicionar: \n')
    tarefa = tarefa.strip()
    if tarefa in tarefas:
        print('Essa tarefa já está na lista\n')
        return tarefa
    elif not tarefa:
        print('Você não digitou nada\n')
        return
    tarefas.append(tarefa)

def desfazer():
    tarefa_para_desfazer = tarefas.pop()
    tarefas_refazer.append(tarefa_para_desfazer)

def refazer():
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer\n')
        return
    
    tarefa_para_refazer = tarefas_refazer.pop()
    tarefas.append(tarefa_para_refazer)
    
def limpar():
    os.system('cls')
    return


while True:
    
    comandos = {
        'listar': lambda: listar(tarefas),
        'refazer': lambda: refazer(),
        'desfazer': lambda: desfazer(),
        'limpar': lambda: limpar(),
        'adicionar': lambda: adicionar(),
    }

    tarefa = input('\nDigite uma tarefa ou comando: \n\n listar | adicionar | desfazer | refazer | limpar\n\n').strip()  
    comando = comandos.get(tarefa)() if tarefa and comandos[tarefa] else print('Você não digitou uma tarefa válida')
   



#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer()
#         continue
#     elif tarefa == 'refazer':
#         refazer()
#         continue
#     elif tarefa == 'adicionar':
#         adicionar()
#         continue
 
#     print('Você não digitou nada\n')
        