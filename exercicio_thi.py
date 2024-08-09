
# galão = 3,6 litros custando 25
# lata = 18 litros custando 80
# 1 litro para cada 6 metros quadrado
"""
litros que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
area = float(input('Digite a área para pintar em metros: '))

lata_preco = 80
galao_preco = 25
lata = 0
galao = 0
litros = area / 6

def calcular_apenas_lata(area):

    if litros % 18 > 0:
          lata = (litros // 18 ) + 1
          print(f'A quantidade de latas vai ser {lata:.0f}')
          return
    lata = litros / 18
    print(f'A quantidade de latas vai ser {lata:.0f}')
    preco_lata = lata * 80
    print(f'O custo vai ser de R${preco_lata:.0f}')

    

def calcular_apenas_galao(area):

    if litros % 3.6 > 0:
          galao = (litros // 3.6 ) + 1
          print(f'Você vai precisar de {galao}')
    preco_galao = galao * 25
    print(f'O custo vai ser de R${preco_galao:.0f}')

def calcular_tudo(area):
    area = area + (area * 0.10)
    lata = litros // 18
    resto = litros % 18
    galao = (resto // 3.6 + 1) if (resto % 3.6 > 0) else (resto / 3.6)
    print(f'O número de latas usados foi {lata:.0f} e de galões foi {galao:.0f}')


calcular_tudo(area)