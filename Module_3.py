# Problem 1
A = int(input())
B = tuple(map(int, input().split()))
C = int(input())
D = tuple(sorted(map(int, input().split())))
j, result = 0, 0
for i in range(A):
    while j < C:
        if D[j] == B[i]:
            result += i + 1
            j += 1
        elif D[j] < B[i]:
            j += 1
        else:
            break
    if j == C:
        break
print(result)

# Problem 2
N = int(input())
for i in range(N):
    L = tuple(sorted(map(int, input().split())))
    j = 0
    while j < len(L):
        M = L[j]
        Cont = 1
        while True:
            if j == len(L)-1:
                break
            if L[j+1] == M:
                Cont += 1
                j += 1
            else:
                break
        j += 1
        print(Cont, end=' ')
    print()

# Problem 3
from bisect import bisect
C = int(input())
for i in range(C):
    Caso = tuple(map(int, input().split()))
    Conj = tuple(map(int, input().split()))
    Primi = True
    j = 1
    while j < (Caso[1]//2)+1:
        # Verificamos si es divisor del numero
        if Caso[1] % j == 0:
            # Verificamos si el objeto esta en el arreglo
            if Conj[bisect(Conj,j)-1] != j:
                Primi = False
                break
            else:
                j += 1
        else:
            j += 1
    if Primi:
        print('Es PrimiConjunto')
    else:
        print('No es PrimiConjunto')

# Problem 4
from bisect import bisect
Carretera = int(input())
Postes = tuple(sorted(map(int, input().split())))
P = int(input())
for i in range(P):
    Par = tuple(map(int, input().split()))
    Dist = 0
    Ps1 = bisect(Postes, Par[0])
    Ps2 = bisect(Postes, Par[1])
    print(str(abs(Ps2-Ps1)), 'kms')

# Problem 5



# Problem 6
C = int(input())
for i in range(C):
    Caso = tuple(sorted(map(int, input().split(', '))))
    # Asignamos un perro a cada fila, a la izquierda el menos pesado
    Der = Caso[-1]
    Izq = Caso[0]
    j, k = 1, -2
    jaj = len(Caso)+k
    while j != len(Caso)+k+1:
        if Izq < Der:
            Izq += Caso[j]
            j += 1
        elif Izq >= Der:
            Der += Caso[k]
            k -= 1
    print(abs(Izq-Der))