# Problem 2: La magia del chisme
from collections import deque
class Nodo:
    def __init__(self):
        self.visitado = False
        self.amigos = set()
        self.chisme = -1


P =  int(input())
comunidad = [Nodo() for j in range(P)]
for i in range(P):
    amiguitos = tuple(map(int, input().split()))
    if amiguitos[0] == -1:
        continue
    for elem in amiguitos:
        comunidad[i].amigos.add(comunidad[elem])
        comunidad[elem].amigos.add(comunidad[i])
casos = tuple(map(int, input().split(", ")))
for a in casos:
    comunidad[a].visitado = True
    comunidad[a].chisme = 0
    cola = deque()
    cola.append(comunidad[a])
    dia = 0
    dias = {}
    while cola:
        dia += 1
        k = len(cola)
        chismorreados_dia = 0
        for j in range(k):
            u = cola.popleft()
            for elem in u.amigos:
                if not elem.visitado:
                    elem.visitado = True
                    elem.chisme = u.chisme + 1
                    cola.append(elem)
                    chismorreados_dia += 1
        dias[dia] = chismorreados_dia
    if len(dias.values()) == 1:
        print(0)
    else:
        print(list(dias.keys())[list(dias.values()).index(max(dias.values()))], max(dias.values()))

    for persona in comunidad:
        persona.visitado = False
        persona.chisme = -1