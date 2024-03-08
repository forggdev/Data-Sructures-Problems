# Problem 5: Encontrando la mediana
from bisect import bisect_left
N = int(input())
L = []
while True:
    M = int(input())
    if M == 0:
        break
    L.insert(bisect_left(L,M),M)
    if len(L) % N == 0:
        Y = len(L)//2
        if len(L) % 2 == 1:
            print(L[Y])
        else:
            if (L[Y] + L[Y-1]) % 2 == 0:
                print(int((L[Y] + L[Y-1])/2))
            else:
                print(str(L[Y] + L[Y - 1]) + '/2')