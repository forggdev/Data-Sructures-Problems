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


# Problem 2: Torre de Saruman
from collections import deque
C = int(input())
for i in range(C):
    Torre = deque()
    Piezas = tuple(map(int, input().split()))
    for j in range(len(Piezas)):
        Torre.append(Piezas[j])
    while len(Torre) > 1:
        if Torre[-1] % 2 == Torre[-2] % 2:
            Torre.append((Torre.pop()+Torre.pop())/2)
        else:
            break
    print(len(Torre), int(Torre[-1]))


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


# Problem 4: Compilador
from collections import deque
C = int(input())
for i in range(C):
    Abiertos = deque()
    Linea = tuple(input().split()[:-1:])
    Correcto = True
    for j in range(len(Linea)):
        if Linea[j] in ('{','[','('):
            Abiertos.append(Linea[j])
        else:
            if len(Abiertos) == 0:
                Correcto = False
                break
            elif Abiertos[-1] + Linea[j] not in ('{}', '[]', '()'):
                Correcto = False
                break
            else:
                Abiertos.pop()
    if Correcto:
        print('correcta')
    else:
        print('incorrecta')


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


# Problem 6

