# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipução de arquivos PDF feita em Python puro, gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir dados de arquivos PDF, assim como adicionar anotações, transformar páginas, extrair texto e imagens, manipular metadados e mais.
# A documentação contém todas as  informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0
from pathlib import Path
from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'focus.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

print(page0.extract_text())
with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)