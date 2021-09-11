while True:
    n,m = map(int, input().split(" "))
    soma = 0
    if n <= 0 or m <= 0:
        break
    
    if n>m:
        for x in range(m,n+1,1):
            soma = soma+x
            print(x,end=' ')
            


    if n<m:
        for x in range(n,m+1,1):
            soma = soma+x
            print(x,end=' ')

    print('Sum={}'.format(soma))
            


    
