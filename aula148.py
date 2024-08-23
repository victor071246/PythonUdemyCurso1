# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e retornar o novo objeto. Por isso, o new recebe cls
# __new__ Deve retornar o novo objeto
# __init__ é o método rensposável por inicializar a instância. Por isso, init recebe self
# __init__ Não deve retornar nada (None)
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.x = 213
        return instancia

    def __init__(self, x):
        self.x = x
        print(self)

    def __repr__(self):
        return F'A()'
    
a = A(123)
print(a.x)