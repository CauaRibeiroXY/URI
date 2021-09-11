import math
qtd = int(input())

def cMatriz(m):
    n = int(m)
    matriz=[]
    for i in range(0,n):
        matriz.append([])
        for j in range(0,n):
            matriz[i].append(0)
    
    return matriz

for i in range(0,qtd):
    posI = int(input())
    vertice, aresta = input().split(' ')
    tamMatriz = math.sqrt(int(vertice))
    matriz = cMatriz(tamMatriz)
    for l in matriz:
        print(matriz)
    for l in range(0,int(aresta)):
        inicio,fim = input().split(' ')
        matriz[int(inicio)-1][int(fim)-1]+=1
    for l in matriz:
        print(matriz)


