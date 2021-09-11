i = 0
j = 0
lista = []

n = float(input())
lista.append(n)
soma = n

while True:
    soma = soma/2
    lista.append(soma)
    if len(lista) == 100:
        break

while (j < 100):

    print('N[{}] = {:.4f}'.format(j,lista[j]))
    j = j+1

