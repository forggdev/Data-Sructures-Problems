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