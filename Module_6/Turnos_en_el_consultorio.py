# Problem 1: Turnos en el Consultorio
import heapq as hpq
Q = []
Last = 0
while True:
    N = input()
    if N == 'end':
        break
    if N == 'sig':
        if Q:
            Last = hpq.heappop(Q)
    else:
        hpq.heappush(Q, int(N))
print(Last)