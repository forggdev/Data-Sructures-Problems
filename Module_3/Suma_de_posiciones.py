# Problem 1
A = int(input())
B = tuple(map(int, input().split()))
C = int(input())
D = tuple(sorted(map(int, input().split())))
j, result = 0, 0
for i in range(A):
    while j < C:
        if D[j] == B[i]:
            result += i + 1
            j += 1
        elif D[j] < B[i]:
            j += 1
        else:
            break
    if j == C:
        break
print(result)