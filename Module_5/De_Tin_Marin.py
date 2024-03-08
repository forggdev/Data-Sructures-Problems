# Problem 2: De Tin Marin
C = int(input())
for _ in range(C):
    N, K = tuple(map(int, input().split()))
    L = [i+1 for i in range(N)] # We enumerate the students
    Pos = (K - 1) % N
    while len(L) > 1:
        K =  (L.pop(Pos) % len(L))
        K = 1 if K == 0 else K
        Pos += (K - 1)
        Pos = (Pos % len(L)) if Pos >= len(L) else Pos
    print(L[0])