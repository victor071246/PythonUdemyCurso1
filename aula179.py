# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o csv em formato de dicionário
import csv
from pathlib import Path

from aulas.aula136 import Endereco

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    # print(next(leitor))
    for linha in leitor:
        print(linha['Nome', linha['Idade'], linha['Endereco']])