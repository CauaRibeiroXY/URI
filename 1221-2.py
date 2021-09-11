from math import sqrt
T = int(input())

def isPrime_fast(num):
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True


for n in range(T):
    num = int(input())
    print("Prime") if num >= 2 and isPrime_fast(num) else print("Not Prime")
    