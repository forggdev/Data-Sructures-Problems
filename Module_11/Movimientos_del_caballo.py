# Problem 6: Movimientos del caballo
from collections import deque


class Nodo:
    def __init__(self, pos):
        self.pos = pos
        self.visitado = False
        self.conectados = []
        self.saltos = 0


valores = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
tablero = [Nodo(i) for i in range(64)]
for i in range(8):
    for j in range(8):
        kk = i*8 + j
        if i > 1:
            if j > 0:
                tablero[i * 8 + j].conectados.append(tablero[(i - 2) * 8 + j - 1])
            if j < 7:
                tablero[i * 8 + j].conectados.append(tablero[(i - 2) * 8 + j + 1])
        if i < 6:
            if j > 0:
                tablero[i * 8 + j].conectados.append(tablero[(i + 2) * 8 + j - 1])
            if j < 7:
                tablero[i * 8 + j].conectados.append(tablero[(i + 2) * 8 + j + 1])
        if j > 1:
            if i > 0:
                tablero[i * 8 + j].conectados.append(tablero[(i - 1) * 8 + j - 2])
            if i < 7:
                tablero[i * 8 + j].conectados.append(tablero[(i + 1) * 8 + j - 2])
        if j < 6:
            if i > 0:
                tablero[i * 8 + j].conectados.append(tablero[(i - 1) * 8 + j + 2])
            if i < 7:
                tablero[i * 8 + j].conectados.append(tablero[(i + 1) * 8 + j + 2])
for i in range(int(input())):
    partida, llegada = input().split()
    partida1, partida2 = valores[partida[0]], int(partida[1]) - 1
    llegada1, llegada2 = valores[llegada[0]], int(llegada[1]) - 1
    a = tablero[partida1 * 8 + partida2]
    a.saltos = 0
    a.visitado = True
    cola = deque()
    cola.append(a)
    while cola:
        u = cola.popleft()
        if tablero[llegada1 * 8 + llegada2] == u:
            break
        for v in u.conectados:
            if not v.visitado:
                v.visitado = True
                v.saltos = u.saltos + 1
                cola.append(v)
    print(tablero[llegada1 * 8 + llegada2].saltos)
    for elem in tablero:
        elem.saltos = 0
        elem.visitado = False
