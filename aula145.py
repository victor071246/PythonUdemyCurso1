# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *args (ilimitado de argumentos posicionais)
# *kwargs (ilimitado de argumentos nomeados)
# Positional-only parameters (/) - Tudo antes da barra deve ser apenas posicional.
# PEP 570 - Python Positional Only Parameters
# http://peps.python.org/pep-0570
# Keyword Only Arguments (*) - * sozinho NÃO SUGA valores.
# PEP 3102 - Keyword-Only arguments
# http://peps.python.org/pep-3102/
def soma(*args):
    print(sum(args))

soma(1)
soma(1, 2, 3)