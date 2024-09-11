# Problem 1: Paulina Bailarina
from collections import deque
class Nodo:
    def __init__(self):
        self.paulina = -1
        self.visitado = False
        self.bailados = []

C =  int(input())
for i in range(C):
    I, B = map(int, input().split(", "))
    participantes = [Nodo() for j in range(I)]
    for k in range(B):
        pareja1, pareja2 = map(int, input().split())
        participantes[pareja1].bailados.append(pareja2)
        participantes[pareja2].bailados.append(pareja1)
    for ii in range(I):
        cola = deque()
        participantes[0].visitado = True
        participantes[0].paulina = 0
        cola.append(participantes[0])
        while cola:
            u = cola.popleft()
            for elem in u.bailados:
                if not participantes[elem].visitado:
                    participantes[elem].visitado = True
                    participantes[elem].paulina = u.paulina + 1
                    cola.append(participantes[elem])
    print("fiesta {}:".format(i+1))
    for jj in range(1,I):
        if participantes[jj].visitado:
            print(jj, participantes[jj].paulina)
        else:
            print(jj, "INF")
    print()
