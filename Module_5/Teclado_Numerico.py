# Problem 3: Teclado Numerico
L = []
while True:
    N = tuple(input().split())
    if N[0] == 'end':
        break
    if N[0] == 'C':
        if len(L) >= 1:
            L.pop()
    elif N[0] == 'D':
        if int(N[1]) <= len(L):
            L = L[:len(L)-int(N[1]):]
    elif N[0] == 'M':
        if int(N[2]) <= len(L):
            Imp = [elem for elem in L[int(N[1]) - 1:int(N[2]):]]
            for i in range(len(Imp)): print(Imp[i], end='')
            print()
    else:
        L.append(int(N[0]))