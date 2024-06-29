a = 'AAAAA'
b = 'BBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(nome1= a, nome2=b, nome3=c)
#tudo o que vem depois do parametro nomeado, tem que ser um parametro nomeado
#método é uma função que está dentro de um objeto

print(formato)
