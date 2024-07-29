# Introdução às Generator Functions in Python
# generator = (n for n in range(100000))

def generator(n=0, maximum=10):
    while True:
        yield n

        if n > maximum:
            return
        
        n += 1

gen = generator(maximum=1000000)
for n in gen:
    print(n)