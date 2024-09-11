# Problem 3: Juego de Tronos Criollo
from collections import deque
class Nodo:
    def __init__(self):
        self.visitado = False
        self.familia = set()

C = int(input())
for i in range(C):
    R = int(input())
    pueblo = {}
    for j in range(R):
        doc1, doc2 = map(int, input().split())
        if doc1 not in pueblo:
            pueblo[doc1] = Nodo()
        if doc2 not in pueblo:
            pueblo[doc2] = Nodo()
        pueblo[doc1].familia.add(doc2)
        pueblo[doc2].familia.add(doc1)
    fam = []
    for key in pueblo.keys():
        if not pueblo[key].visitado:
            c = 0
            pila = deque()
            pila.append(pueblo[key])
            while pila:
                u = pila.pop()
                if not u.visitado:
                    u.visitado = True
                    c += 1
                    for elem in u.familia:
                        if not pueblo[elem].visitado:
                            pila.append(pueblo[elem])
            fam.append(c)
    print(len(fam), max(fam))