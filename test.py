# Problem 6: Torre de Hanoi
from collections import deque
Casos = int(input())
for i in range(Casos):
    Discos = int(input())
    A = deque([i for i in range(Discos,0,-1)])
    B,C = deque(), deque()
    Incorrecto = False
    
    while True:
        Mov = tuple(input().split())
        if Mov[0] == 'X':
            break
        elif not Incorrecto:
            if Mov[0] == 'A':
                if A:
                    Disco = A.pop()
                else:
                    Disco = 0
                    Incorrecto = True
            elif Mov[0] == 'B':
                if B:
                    Disco = B.pop()
                else:
                    Disco = 0
                    Incorrecto = True
            else:
                if C:
                    Disco = C.pop()
                else:
                    Disco = 0
                    Incorrecto = True

            if Mov[1] == 'A':
                if A:
                    if Disco > A[-1]:
                        Incorrecto = True
                    else:
                        A.append(Disco)
                else:
                    A.append(Disco)
            elif Mov[1] == 'B':
                if B:
                    if Disco > B[-1]:
                        Incorrecto = True
                    else:
                        B.append(Disco)
                else:
                    B.append(Disco)
            else:
                if C:
                    if Disco > C[-1] and C:
                        Incorrecto = True
                    else:
                        C.append(Disco)
                else:
                    C.append(Disco)

    if Incorrecto:
        print('secuencia invalida')
    elif C == deque([i for i in range(Discos,0,-1)]):
        print('soluciona la torre')
    else:
        print('no soluciona la torre')