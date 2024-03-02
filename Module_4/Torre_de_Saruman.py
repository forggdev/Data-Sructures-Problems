# Problem 2: Torre de Saruman
from collections import deque
C = int(input())
for i in range(C):
    Torre = deque()
    Piezas = tuple(map(int, input().split()))
    for j in range(len(Piezas)):
        Torre.append(Piezas[j])
    while len(Torre) > 1:
        if Torre[-1] % 2 == Torre[-2] % 2:
            Torre.append((Torre.pop()+Torre.pop())/2)
        else:
            break
    print(len(Torre), int(Torre[-1]))