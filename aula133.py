# Encapsulamento (modificadores de acesso: public, protected)
# Python NÃO TEM modificadores de acesso mas podemos seguir as seguintes convenções:
# (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não deve ser usado fora da classe ou em suas subclasses
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome__attr_ou_method
#       só deve ser usado na classe em que foi declarado
from functools import partial


class Foo:
    def __init__(self):
        self.public - 'isso é publico'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é privado'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('método protegido')
        return 'método protegido'
    
    def __metodo_private(self):
        print('método privado')
        return 'método privado'

f = Foo()
# print(f._protected)
# print(f._metodo_protected())
# print(f.public)
# print(f.metodo_publico)
print(f._Foo__metodo_privado())