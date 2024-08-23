# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe "callable"

from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwds):
        print(*args, ' está chamando ', self.phone)

call1 = CallMe('23945876545')
call1('Luiz Otávio')