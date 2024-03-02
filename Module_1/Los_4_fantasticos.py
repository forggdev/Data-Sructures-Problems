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