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
