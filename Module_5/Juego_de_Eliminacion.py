# Problem 4: Juego de Eliminacion
L = []
while True:
    N = int(input())
    if N == 0:
        break
    if N in L:
        L.remove(N)
    elif N + 1 in L:
        L.remove(N + 1)
    elif N - 1 in L:
        L.remove(N - 1)
    else:
        L.append(N)
if len(L) == 0:
    print(0)
else:
    for i in L:
        print(i, end=' ')
