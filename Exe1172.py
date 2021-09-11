i = 0
lista = []
j = 1
while (i < 10):
    n = int(input())
    if n <= 0:
        lista.append(1)
    else:
        lista.append(n)
  
    i = i+1      

for j in range(10):
    print('X[{}] = {}'.format(j,lista[j]))

