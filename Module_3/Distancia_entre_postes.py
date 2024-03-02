# Problem 4
from bisect import bisect
Carretera = int(input())
Postes = tuple(sorted(map(int, input().split())))
P = int(input())
for i in range(P):
    Par = tuple(map(int, input().split()))
    Dist = 0
    Ps1 = bisect(Postes, Par[0])
    Ps2 = bisect(Postes, Par[1])
    print(str(abs(Ps2-Ps1)), 'kms')