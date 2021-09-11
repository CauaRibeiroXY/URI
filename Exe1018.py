n = int(input())

troco = n

cem = troco//100
troco = troco-(cem*100)

cin = troco//50
troco = troco-(cin*50)

vinte = troco//20
troco = troco-(vinte*20)

dez = troco//10
troco = troco-(dez*10)

cinco = troco//5
troco = troco-(cinco*5)

dois = troco//2
troco = troco-(dois*2)

print(n)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cin))
print('{} nota(s) de R$ 20,00'.format(vinte))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(troco))