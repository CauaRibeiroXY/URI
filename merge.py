vetor = input().split(',')

def Merges(v): # ini = 2 fim =3 

    if(len(v)>1):
        meio = int(len(v)/2)
        listaDaEsquerda = v[:meio]


        listaDaDireita = v[meio:]

        Merges(listaDaEsquerda)
        Merges(listaDaDireita)
        i=0
        j=0
        k=0
    
        while(i < len(listaDaEsquerda) and j < len(listaDaDireita)):
            if(listaDaEsquerda[i]<listaDaDireita[j]):
                v[k]=listaDaEsquerda[i]
                i+=1
            else:
                v[k]=listaDaDireita[j]
                j+=1
            k+=1
        while(i < len(listaDaEsquerda) ):
            v[k]=listaDaEsquerda[i]
            i+=1
            k+=1
        while(i < len(listaDaDireita) ):
            v[k]=listaDaDireita[j]
            j+=1
            k+=1
        return v



    
    
    
        
resultado=Merges(vetor)
print(resultado)

   