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