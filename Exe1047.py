hi,mi,hf,mf = map(int, input().split(" "))

if hi == hf:
    if mi == mf:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif mf>mi:
        tempoh = hf-hi
        tempom = mf-mi
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempoh,tempom))   
    else:
        tempoh = 23
        tempom = (60-mi)+mf
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempoh,tempom))   
else:
    if hi>hf:
        tempoh = (24-hi)+hf
    else:
        tempoh = hf-hi
    if mi>mf:
        tempom = (60-mi)+mf
    else:
        tempom = mf-mi
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempoh,tempom))



