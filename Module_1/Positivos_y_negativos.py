# Problem 3
A = int(input())
Pos = 0
Neg = 0
for i in range(A):
    B = int(input())
    if B < 0:
        Neg += B
    else:
        Pos += B
print("positivos " + str(Pos) + ", negativos " + str(Neg))