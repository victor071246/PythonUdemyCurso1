# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só precisa herdar de alguma exceção de linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error no final)
# Levantando (raise) / Lançando trhow exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...