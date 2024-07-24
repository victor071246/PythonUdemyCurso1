"""
Escopo de funções em python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcançável.
O escopo local é o escopo onde apenas nomes no mesmo do mesmo escopo local podem ser alcançados
Não temos acessos a nomes de escopo internos nos escopos externos
A palavra global faz a mesma variável do escopo interno ser a mesma do escopo interno
"""


x = 1

def escopo():
    # global x
    x = 10
    print(x)

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    
    print(x)

print(x)
escopo()
print(x)