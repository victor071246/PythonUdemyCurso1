# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só precisa herdar de alguma exceção de linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error no final)
# Levantando (raise) / Lançando trhow exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuErro(Exception):
    ...

class OutroErro(Exception):
    ...

def levantar():
    exception_ =  MeuErro('A mensagem do meu erro')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_
try:
    levantar()
except (MeuErro, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ =  OutroErro('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error