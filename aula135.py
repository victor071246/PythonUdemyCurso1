# Relações entre classes: associação, agregação e composição
# Entre dois ou mais objetos, cada objeto terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum(p.preco for p in self._produtos)
    
    def interir_produtos(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        # self._produtos.extend(produtos)
        self._produtos += produtos
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.interir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())