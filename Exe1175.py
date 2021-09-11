listaX = []
liY = []

i = 0
j = 0

while (i < 20):
    n = float(input())
    listaX.append(n)
    i = i+1

i = 0
while (i < 20):
    liY.append(listaX.pop())
    
    i = i+1

while (j < 20):

    print('N[{}] = {:.0f}'.format(j,liY[j]))
    j = j+1