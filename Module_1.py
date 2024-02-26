# Problem 1
A = int(input())
print(A * A)

# Problem 2
A = int(input())
for i in range(A):
    if i % 2 == 0:
        print("Hola mundo")
    if i % 2 == 1:
        print("Hello world")

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

# Problem 4
A = int(input())
if A % 2 == 0:
    print("es multiplo de 2")
elif A % 3 == 0:
    print("es multiplo de 3")
elif A % 5 == 0:
    print("es multiplo de 5")
elif A % 7 == 0:
    print("es multiplo de 7")
else:
    print("no es multiplo de ninguno de los primeros cuatro primos")

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