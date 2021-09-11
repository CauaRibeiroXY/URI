import math
n = int(input())

for i in range(0,n):
    tam = int(input())
    tabuleiro = tam*tam
    grao = 0
    for l in range(0,tam):
        grao += pow(2,l)
    
    grama = grao/12
    kilo = grama/1000
    tonelada = kilo/1000
    print("{:.0f} kg".format(kilo))