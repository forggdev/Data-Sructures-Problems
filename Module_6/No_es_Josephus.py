# Problem 6: No es Josephus
from collections import deque
import heapq as hpq
C = int(input())
for i in range(C):
    N, A, B = map(int, input().split())
    H = [i+1 for i in range(N)]
    hpq.heapify(H)
    while len(H) > 1:
        D = deque()
        for j in range(len(H)):
            D.append(H.pop())
        for k in range(len(D)):
            hpq.heappush(H, (D.pop()*A) % B)
        for jj in range(len(H)//2):
            hpq.heappop(H)
    print(hpq.heappop(H))