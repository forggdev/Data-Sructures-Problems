# Problem 1: Sumatoria de Multiplos
L = []
while True:
    Command = tuple(input().split())
    if Command[0] == 'E':
        break
    if Command[0] == 'A':
        L.append(int(Command[1]))
    else:
        Sum = 0
        Divisor = int(Command[1])
        for i in L:
            if i % Divisor == 0:
                Sum = Sum + int(i)
        print(Sum)
