import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(len(generator)) # Não exibe o dado corretamente

for n in generator:
    print(n)