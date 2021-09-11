N = (int)(input())

for i in range(0,N):
    linha = input()
    maior = 0
    menor = 0
    for l in linha:
        if l == '<':
            menor+=1
        if l == '>':
            if menor != 0:
                maior+=1
                menor-=1
            
    print(maior)
    