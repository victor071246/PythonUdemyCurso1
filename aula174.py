# os + shutil - Apagando e copiando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copys
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Àrvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive\\Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

shutil.move(NOVA_PASTA, NOVA_PASTA + '_teste')