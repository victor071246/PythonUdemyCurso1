# Classes decoradoras (Decorator classes)

from typing import Any


class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

@Multiplicar(100)
def soma(x, y):
    return x + y

dois_mais_dois = soma(2,2)

print(dois_mais_dois)