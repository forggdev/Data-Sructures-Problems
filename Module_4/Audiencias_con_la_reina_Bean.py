# Problem 5: Audiencias con la Reina Bean
from collections import deque
C = int(input())
for i in range(C):
    Personas, Elfo = tuple(map(int, input().split()))
    Fila = deque()
    for j in range(Personas):
        if j == Elfo-1:
            Fila.append('E')
        else:
            Fila.append('P')
    Peticiones = deque(map(int, input().split()))
    Num_Pet = 0
    while True:
        Num_Pet += 1
        if Fila[0] == 'E' and Peticiones[0] == 1:
            break
        else:
            if Peticiones[0] == 1:
                Fila.popleft()
                Peticiones.popleft()
            else:
                Fila.append(Fila.popleft())
                Peticiones.append(Peticiones.popleft()-1)
    print(Num_Pet * 5)