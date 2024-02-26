# Problem 3
C = int(input())
for i in range(C):
    Caso = tuple(map(int, input().split()))
    Conj = tuple(map(int, input().split()))
    Primi = True
    j = 1
    while j <= Caso[1]:
        # Verificamos si es divisor del numero
        if Caso[1] % j == 0:
            # Verificamos si el objeto esta en el arreglo
            if j not in Conj:
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
