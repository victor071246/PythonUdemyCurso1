# Escopo da classe e métodos de classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome
    
        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo alguma {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('carne'))