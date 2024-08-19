# super() é a super classe na sub classe
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')
class B(A):

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa


    atributo_b = 'valor b'
    def metodo(self):
        print('B')
class C(B):
    atributo_c = 'valor c'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print('EI, burlei o sistema.')

    def metodo(self):
        # super().metodo() # B
        # super(A, self).metodo() # A
        # super(B, self).metodo() # object
        A.metodo(self)
        B.metodo(self)
        print('C')

c = C('atributo', 'qualquer')
# print(c.outra_coisa)
c.metodo()
# print(c.atributo)
# print(C.mro())
# c = C()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)