# Problem 5: Deforestacion en el Amazonas
from collections import deque
class Nodo:
    def __init__(self):
        self.visitado = False
        self.conectados = set()
        self.deforestado = False

C = int(input())
for _ in range(C):
    A, B = map(int, input().split())
    adyacencias = []
    for i in range(A):
        adyacencias.append(input())
    bosque = [Nodo() for _ in range(A*B)]
    for i in range(A):
        for j in range(B):
            ind = i*B + j
            if i > 0:
                bosque[ind].conectados.add(bosque[ind - B])
            if i < A-1:
                bosque[ind].conectados.add(bosque[ind + B])
            if j > 0:
                bosque[ind].conectados.add(bosque[ind - 1])
            if j < B-1:
                bosque[ind].conectados.add(bosque[ind + 1])
            if adyacencias[i][j] == 'X':
                bosque[ind].deforestado = True
    areas = []
    for a in bosque:
        if not a.visitado and a.deforestado:
            hec = 0
            pila = deque()
            pila.append(a)
            while pila:
                u = pila.pop()
                if not u.visitado and u.deforestado:
                    u.visitado = True
                    hec += 1
                    for v in u.conectados:
                        if not v.visitado and v.deforestado:
                            pila.append(v)
            areas.append(hec)
    print(max(areas))
