import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(Depositando R${valor}...)')
        return self.saldo

    def detalhes(self, msg: str='') -> None:
        print(f'O seu saldo é {self.saldo:.2f} \n {msg} \n')

class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Sacando R${valor} ...)')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes('Saque negado, valor insuficiente')
        return self.saldo 

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float=0, limite: float=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite 

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(Sacando R${valor:.2f} ...)')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes('Saque negado, valor insuficiente')
        return self.saldo

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(1000)
    cp1.sacar(1)
    print('###')
    cc1 = ContaCorrente(111, 223, 0, 100)
    cc1.sacar(1)
    cc1.depositar(10)
    cc1.sacar(1)
    cc1.sacar(98)
    print('###')