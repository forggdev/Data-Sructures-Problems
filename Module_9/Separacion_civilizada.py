# Problem 5: Separacion Civilizada
F = set()
G = set()
while True:
    N = tuple(input().split())
    if N[0] == '0':
        break
    F.add(int(N[0])) if N[1] == 'F' else G.add(int(N[0]))
GAYS = F & G
for elem in GAYS:
    if elem % 2 == 1:
        F.remove(elem)
    else:
        G.remove(elem)
print(len(F), len(G))