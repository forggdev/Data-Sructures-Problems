# Problem 4: Menor Suma Posible
import heapq as hpq
C = int(input())
for i in range(C):
    L = int(input())
    N = tuple(input().split())
    H = []
    X, Y = '', ''
    for j in range(L):
        hpq.heappush(H, N[j])
    for k in range(L):
        if k % 2 == 0:
            X += hpq.heappop(H)
        else:
            Y += hpq.heappop(H)
    print(int(X) + int(Y))