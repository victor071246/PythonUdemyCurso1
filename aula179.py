# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o csv em formato de dicionário
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r') as arquivo:z