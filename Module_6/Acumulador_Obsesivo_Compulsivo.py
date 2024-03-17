# Problem 3: Acumulador obsesivo compulsivo
import heapq as hpq
C = int(input())
for i in range(C):
    N = tuple(map(int, input().split()))
    H = []
    for j in range(len(N)-1):
        hpq.heappush(H,N[j])
    while len(H) > 2:
        hpq.heappush(H,hpq.heappop(H)+hpq.heappop(H))
    print(hpq.heappop(H), hpq.heappop(H))