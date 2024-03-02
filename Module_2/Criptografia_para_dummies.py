# Problem 3
A = int(input())
for i in range(A):
    Enc = tuple(input().split())
    DesEnc_1 = Enc[::-1]
    for j in range(len(DesEnc_1)//2):
        print(DesEnc_1[2*j+1] + DesEnc_1[2*j], end='')
    if len(DesEnc_1) % 2 == 1:
        print(DesEnc_1[-1], end='')
    print()