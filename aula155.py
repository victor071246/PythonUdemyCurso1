# Metaclasses são o tipo das classes
# Em Python, tudo é um objeto (classes também)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclasse)

# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
# __new__ da class com os argumentos (cria a instância)
# __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__ (cls, *args, **kwargs) (cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários deveriam se preocupar. Se você quer saber se precisa delas, não precisa (as pessoas que realmente precisam delas sabem com certeza que precisam delas e não precisam de uma explicação sobre o porquê)"
# - Tim Peters (CPython Core Developer)
#
def meu_rpr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('MEU NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 123
        cls.__repr__ = meu_rpr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplemented('Implemente falar')

        return cls
    
        def __call__(cls, *args, **kwargs):
            instancia = super().__call__(*args, **kwargs)
            print(instancia.__dict__)

class Pessoa(object, metaclass=Meta):
    falar = 123
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('MEU INIT')

    def falar(self):
        print('Falando...')
    
p1 = Pessoa('Luiz')