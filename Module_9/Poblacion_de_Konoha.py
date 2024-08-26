# Problem 2: Poblacion de Konoha
Konoha = set()
Ded = set()
Ressd = set()
while True:
    N = tuple(input().split())
    if N[0] == 'E':
        break
    if N[0] == 'B':
        if int(N[1]) not in Ded and int(N[1]) not in Ressd:
            Konoha.add(int(N[1]))
    elif N[0] == 'D':
        if int(N[1]) in Konoha:
            Konoha.remove(int(N[1]))
            Ded.add(int(N[1]))
    else:
        if int(N[1]) in Ded:
            Konoha.add(int(N[1]))
print(len(Konoha))