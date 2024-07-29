# dir, hasatrr e gatattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método ', metodo)