lista = []
soma = 0
cont = 0
i = 0

while (i < 6):
    n = float(input())
    
    i = i+1
    if n > 0:
        soma = soma+n
        cont = cont+1

media = soma/cont
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))






