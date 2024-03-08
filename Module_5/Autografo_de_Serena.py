# Problem 6: Autografo de Serena
L = []
while True:
    ID, N = tuple(input().split())
    N = int(N)
    if ID == '0':
        break
    if len(L) < N:
        L.append(N)
    for i in range(len(L)-1,-1,-1):
        if L[i] < len(L):
            L.pop(i)
            break
print(len(L))