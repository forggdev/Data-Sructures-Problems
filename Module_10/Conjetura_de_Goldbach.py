# Problema 6: Conjetura de Goldbach
def criba(n):
    primos = [True for i in range(n+1)]
    p = 2
    primos[0] = False
    primos[1] = False
    while p*p <= n:
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    return primos

criba = criba(10000)
primos = {i for i in range(2, len(criba)) if criba[i]}
primoss = list(primos)
primoss.sort()
for i in range(int(input())):
    N = int(input())
    c = 0
    for elem in primoss:
        if elem > N:
            break
        if N - elem in primos and elem <= N - elem:
            c += 1
    print(c)


