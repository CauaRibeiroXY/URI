i = 0
j = 0
lista = []

while (i < 100):
    n = float(input())
    lista.append(n)
    i = i+1
len(lista)

while (j < 100):

    if lista[j] <= 10:
        print('A[{}] = {:.1f}'.format(j,lista[j]))


    j = j+1




