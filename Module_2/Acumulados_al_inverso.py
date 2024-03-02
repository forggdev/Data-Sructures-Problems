# Problem 1
A = int(input())
N = input()
lista = N.split()
suma = int(lista[-1]) + int(lista[-2])
print(suma)
for k in range(0,A-2,1):
    suma+=int(lista[-3-k])
    print(suma)