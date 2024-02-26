# Problem 1
A = int(input())
N = input()
lista = N.split()
suma = int(lista[-1]) + int(lista[-2])
print(suma)
for k in range(0,A-2,1):
    suma+=int(lista[-3-k])
    print(suma)

# Problem 2
A = int(input())
So, Lar, Is = tuple(map(int, input().split(", "))), tuple(map(int, input().split(", "))), tuple(map(int, input().split(", ")))
SoW, LarW , IsW = 0, 0, 0
for i in range(A):
    sum = int(So[i]) + int(Lar[i]) + int(Is[i])
    if sum%2==So[i]%2:
        SoW += 1
    if sum%2==Lar[i]%2:
        LarW += 1
    if sum%2==Is[i]%2:
        IsW += 1
print("SO:" + str(SoW) + ", LAR:" + str(LarW) + ", IS:" + str(IsW))

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

# Problem 4
A = int(input())
B = tuple(input().split(', '))
C = ''
for i in range(A//2):
    C += B[i] + B[-1-i]
if A % 2 == 1:
    C += B[A//2]
print(C)

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

# Problem 6
A = int(input())
for i in range(A):
    B = int(input())
    Tab = tuple(map(int, input().split()))
    indexes = ()
    movements = 0
    position = 0
    while True:
        movements += 1
        indexes += (position,)
        position += Tab[position]
        if position in indexes or position<0 or position>=len(Tab):
            break
    print(movements)

