# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos um determinado número de coisas.
# Enumns têm membros e seus valores são constantes.
# Enumns em python:
# - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
# - podem ser iterados para retornar seus membros canônicos na ordem de definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Enumns não são classes normais em Python)
# Você poderá usar seu Enum com type annotations, com isinstance e outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name, Classe(valor), Classe['chave']
# valor = Classe.chave.value
import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('lado')
