# Problem 4
A = int(input())
B = tuple(input().split(', '))
C = ''
for i in range(A//2):
    C += B[i] + B[-1-i]
if A % 2 == 1:
    C += B[A//2]
print(C)