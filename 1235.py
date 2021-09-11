N = (int)(input())

for i in range(0,N):
    linha = input()
    aux = ""
    tam= len(linha)
    tam2 = (int)(tam/2)
 
    pilha1 = []
    pilha2 = []

    for l in range(0,tam2):
        pilha1.append(linha[l])
    
        
    for b in range(tam2,tam):
        pilha2.append(linha[b])
   
    
    for l in range(0,tam2):
        aux+=pilha1.pop()
        #print(aux)
    
    for b in range(tam2,tam):
        aux+=pilha2.pop()
       # print(aux)
    print(aux)

