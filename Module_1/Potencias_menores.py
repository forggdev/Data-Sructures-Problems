# Problem 5
A = int(input())
B = int(input())
i = 1
while True:
    if A ** i <= B:
        print(A ** i)
        i += 1
    else:
        break