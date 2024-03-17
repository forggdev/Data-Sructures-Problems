# Problem 2: Lucha de los menores
import heapq as hpq
A,B,C = [], [], []
Ap,Bp,Cp = 0, 0, 0
while True:
    N = input()
    if N == 'fin del juego':
        break
    if N == 'menores':
        if A or B or C:
            Am = hpq.heappop(A) if A else 1001
            Bm = hpq.heappop(B) if B else 1001
            Cm = hpq.heappop(C) if C else 1001
            Min = min(Am,Bm,Cm)
            if Am == Min:
                Ap += 1
            if Bm == Min:
                Bp += 1
            if Cm == Min:
                Cp += 1
    else:
        Eq, V = N.split()
        if Eq == 'A':
            hpq.heappush(A, int(V))
        if Eq == 'B':
            hpq.heappush(B, int(V))
        if Eq == 'C':
            hpq.heappush(C, int(V))

print('Equipo A:', Ap)
print('Equipo B:', Bp)
print('Equipo C:', Cp)
