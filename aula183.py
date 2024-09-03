# string.Template para substituir variáveis em textos
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse de template.
import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'


locale.setlocale(locale.LC_ALL, '')

def converter_para_brl(numero: float | int) -> str:
    brl = 'R$ ' +locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converter_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M. ',
    telefone= '+55 (11) 7890-5432'
)

import json
# print(json.dumps(dados, indent=2, ensure_ascii=False))

texto = '''
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de $valor no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

Atenciosamente,

$empresa
'''

class MyTemplate(string.Template):
    delimiter = '%'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo: 
    texto = arquivo.read()
    # template = string.Template(texto)
    template = MyTemplate(texto)
    print(template.safe_substitute(dados))