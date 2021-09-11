from math import sqrt
n = int(input())

for i in range(0,n):
    p = int(input())
    div = int(p/2)
    raiz = int(sqrt(p)+1)
    c=2
    for l in range(2,raiz):
        if((p%l)==0):
            c=1
    
    if(p==2):
        print("Prime")
        c=0
    if(p==4):
        print("Not Prime")
        c=0
    if(c==2):
        print("Prime")
    if(c==1):
        print("Not Prime")

