# Funções decoradoras e decoradores com classes
def adiciona_repr(cls):
    def meu_rpr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_rpr = f'{class_name}({class_dict})'
        return meu_rpr
    cls.__repr__ = meu_rpr
    return cls

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')