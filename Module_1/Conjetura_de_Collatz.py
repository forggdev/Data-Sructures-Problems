# Problem 6
A = int(input())
while True:
    print(A)
    if A == 1:
        break
    elif A % 2 == 0:
        A = int(A / 2)
    else:
        A = 3 * A + 1