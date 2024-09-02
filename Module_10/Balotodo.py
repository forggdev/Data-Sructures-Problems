# Problem 3: Balotodo

M = int(input())
win = set()
jug = {}
c = 0
while True:
    N = input().split()
    if N[0] == 'end':
        break
    if N[0] == 'winner':
        win.add(int(N[1]))
    else:
        if int(N[1]) not in jug:
            jug[int(N[1])] = 1
        else:
            jug[int(N[1])] += 1
        if int(N[1]) in win:
            print(int(N[1]), M // (len(win) * jug[int(N[1])]))
            c += 1
if len(win) == 0 or c == 0:
    print(0)