# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptionss
def erro_divide_por_zero(d):
    if d == 0:
      raise ZeroDivisionError('Não é possível dividir um número por zero')
    return True

def deve_ser_int_ou_float(n):
     tipo_n = type(n)
     if not isinstance(n, (float, int)):
          raise TypeError(
               f'{n} deve ser int ou float'
               f'{tipo_n.__name__} enviado'
          )

def divide(n, d):
        erro_divide_por_zero(d)
        deve_ser_int_ou_float(n)
        deve_ser_int_ou_float(d)

        return n / d

print(divide(8, 0))