# Context Manager com classes
# Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o Python vai usar.
# Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no tipo, mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o traceback. Se ele retornar True, a exceção no with será suprimida.
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo_modo, modo):
        print('INIT')
        self.caminho_arquivo = caminho_arquivo_modo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
        
    
    def __exit__(self, class_, exception_class, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()

        # raise exception_class(*exception_class).with_traceback(traceback_)

        # print(exception_class)
        # print(exception_)
        # print(traceback_)

        exception_.add_note('Minha nota')

        raise ConnectionError('Não deu para conectar')

        # return True # Tratei a exceção

# instancia = MyOpen('aula149.txt', 'w')
# with instancia as arquivo:
#     print('With', alguma_coisa)

with MyOpen('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)