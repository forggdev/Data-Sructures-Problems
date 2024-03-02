# Problem 5
A = int(input())
for i in range(A):
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))
    D = ()
    for k in range(B[0]):
        sum = 0
        for j in range(B[1]):
            if j % B[0] == k:
                sum += C[j]
        D += (sum,)
    print(max(D)-min(D))