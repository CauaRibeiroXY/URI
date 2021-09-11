i = 0
j = 0
matriz = []
linhaX = int(input())
ope = input()

for i in range(12):
    linha = []
    for j in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)


soma = 0
media = 0
for a in range(12):
    for b in range(12):
        if a == linhaX:
            soma+=matriz[a][b]

media = soma/12

if ope == "S":
    print('{:.1f}'.format(soma))
elif ope == "M":
    print('{:.1f}'.format(media))


