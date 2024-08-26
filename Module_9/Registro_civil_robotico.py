# Problem 4: Registro Civil Robotico
rbts = set()
F = int(input())
for i in range(F):
    rbts.add(i+1)
while True:
    N = tuple(input().split())
    if N[0] == '#':
        break
    if N[0] == 'new':
        bby = int(N[1]) + int(N[2])
        if bby not in rbts:
            rbts.add(bby)
        else:
            while bby in rbts:
                bby += 1
            rbts.add(bby)
    else:
        if int(N[1]) in rbts:
            print('existe')
        else:
            print('no existe')