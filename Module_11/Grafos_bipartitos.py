# Problem 4: Grafos Bipartitos
from collections import deque
class Nodo:
    def __init__(self):
        self.visitado = False
        self.conectados = set()
        self.coloreado = 0

C = int(input())
for i in range(C):
    N, M = map(int, input().split())
    grafo = [Nodo() for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split(', '))
        grafo[u-1].conectados.add(v-1)
        grafo[v-1].conectados.add(u-1)
    bipartito = True
    for a in grafo:
        if a.coloreado == 0:
            pila = deque()
            pila.append(a)
            while pila:
                u = pila.pop()
                if not u.visitado:
                    u.visitado = True
                    if u.coloreado == 0:
                        u.coloreado = 1
                    for elem in u.conectados:
                        if not grafo[elem].visitado:
                            if grafo[elem].coloreado == u.coloreado:
                                bipartito = False
                                break
                            if grafo[elem].coloreado == 0:
                                if u.coloreado == 1:
                                    grafo[elem].coloreado = 2
                                else:
                                    grafo[elem].coloreado = 1
                            pila.append(grafo[elem])
    if bipartito:
        print("bipartito")
    else:
        print("no bipartito")
