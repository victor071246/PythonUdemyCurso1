import copy

from dados_aula_100 import produtos

# Aumente os preços dos produtos a seguir em 10%
# Gere novos produtos por deep_copy (cópia profunda)
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
    # fazer a list comprehension
]


# print(*produtos, sep='\n')
# print()
# print(*novos_produtos , sep='\n')

# Ordene os produtos por nome descrente (maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)

# Ordene os produtos por preço crescente (do menor para o maior)
# Gere os produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_nome_ao_contrario = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print(*produtos_ordenados_por_preco, sep='\n')