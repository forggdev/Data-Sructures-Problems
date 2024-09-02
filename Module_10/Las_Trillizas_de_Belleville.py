# Problem 2: Las Trillizas de Belleville
N = tuple(map(int, input().split()))
A = []
for i in range(N[0]):
    A.append(int(input()))
B = set(A)    
ternas = []
for i in range(len(A)-1):
    for j in range(i + 1, len(A)):
        res = N[1] - A[i] - A[j]
        if res in B:
            if A[i] == res or A[j] == res:
                continue
            terna = [A[i], A[j], res]
            terna.sort()
            if terna not in ternas:
                ternas.append(terna)
ternas.sort()
if len(ternas) == 0:
    print("No hay trillizas")
else:
    for i in range(len(ternas)):
        print(ternas[i][0], ternas[i][1], ternas[i][2])


