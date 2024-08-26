# Problem 1: Coleccion de Pokemones
F = set()
V = set()
while True:
    N = tuple(input().split())
    if N[0] == '#':
        break
    F.add(int(N[1])) if N[0] == "F" else V.add(int(N[1]))
print(len(F), len(V), len(F | V))