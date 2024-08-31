# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/Exemplo
# \Users\luizotavio\Desktop\Exemplo
import os

caminho = os.path.join('C:\\Users\\victo\\OneDrive')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print('   ',pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for arquivo in os.listdir(caminho_completo_pasta):
        print(arquivo)