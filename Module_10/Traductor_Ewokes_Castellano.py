# Problem 1: Traductor Ewokes Castellano
dick = {}
for i in range(int(input())):
    E = input().split()
    dick[E[0]] = E[1]
while True:
    S = input()
    if S == '#':
        break
    if S in dick:
        print(dick[S])
    else:
        print("Entrada no encontrada")
