def sort(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and len(array[p - 1]) > len(current_element):
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element

while True:
    N = int(input())
    if N == 0:
        break
    s = []
    verifica = []
    linhas = []
    cont = 0
    for i in range(0,N):
        linha= input()
        linhas.append(linha)
     
    sort(linhas)
    
    for i in range(0,N):
        for j in range(i,N):
            if linhas[i] in linhas[j] and verifica[i] == 0:
                cont+=1
    print("TESTE: ",cont)




