# Problem 1: Fila de Revendedores
from collections import deque
Personas, Boletas = tuple(map(int, input().split()))
Revendedores, j = deque(), 0
for i in range(Personas):
    Revendedores.append(tuple(map(int, input().split())))
while len(Revendedores) != 0:
    j += 1
    if j % 5 != 0:
        Boletas -= Revendedores[0][1]
        if Boletas <= 0:
            break
        Revendedores.append(Revendedores.popleft())
    else:
        Boletas -= Revendedores[0][1]
        if Boletas <= 0:
            break
        Revendedores.popleft()
if len(Revendedores) == 0 and Boletas > 0:
    print('quedaron boletas disponibles')
else:
    if Boletas == 0:
        print(Revendedores[0][0], Revendedores[0][1])
    else:
        print(Revendedores[0][0], Revendedores[0][1]+Boletas)