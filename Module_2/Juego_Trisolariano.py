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