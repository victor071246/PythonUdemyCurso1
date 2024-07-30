#try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
    # open
except ZeroDivisionError as e:
    print('Número não pode ser dividido por zero')
    print(e)
    print(e.__class__.__name__)
except IndexError as error:
    print('Index error')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:    
    print('FECHAR ARQUIVO')