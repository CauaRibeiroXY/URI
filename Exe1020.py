n = int(input())

cont = n
ano = cont//365
cont = cont-(ano*365)

mes = cont//30
cont = cont-(mes*30)

print('{} anos (s)'.format(ano))
print('{} mes (es)'.format(mes))
print('{} dias (s)'.format(cont))
