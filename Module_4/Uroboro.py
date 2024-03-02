# Problem 3: Uróboro
from collections import deque
Ouroboros = deque()
while True:
    Msje = tuple(input().split())
    if Msje[0] == 'termina':
        break
    elif Msje[0] == 'agrega':
        Ouroboros.append(int(Msje[1]))
    else:
        if len(Ouroboros) == 0:
            continue
        elif len(Ouroboros) == 1:
            Ouroboros.pop()
            continue
        elif Ouroboros[0] > Ouroboros[-1]:
            Ouroboros.pop()
        else:
            Ouroboros.popleft()
if len(Ouroboros) == 0:
    print('uroboro vacio')
else:
    print('cabeza', Ouroboros[0], 'cola', Ouroboros[-1])