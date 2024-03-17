# Problem 5: Sintetizador Digital Periodico
import heapq as hpq
Dur = int(input())
T = int(input())
H = []
for i in range(T):
    Tono= tuple(map(int, input().split()))
    hpq.heappush(H,(Tono[1],Tono[2]))
while True:
    if H[0][0] > Dur:
        break
    S = hpq.heappop(H)
    print(S[0])
    hpq.heappush(H,(S[0]+S[1],S[1]))