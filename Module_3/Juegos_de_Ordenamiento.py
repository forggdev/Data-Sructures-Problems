# Problem 5
C = int(input())
for k in range(C):
    Fila = list(map(int, input().split()))
    N = len(Fila)
    Mov = 0
    for i in range(N):
        for j in range(0, N - i - 1):
            if Fila[j] > Fila[j + 1]:
                Fila[j], Fila[j + 1] = Fila[j + 1], Fila[j]
                Mov += 1
    print(Mov)