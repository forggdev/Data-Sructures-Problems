import random
b = []
for i in range(20):
    a = random.randint(0,99)
    if a not in b:
        b.append(a)
        print(a, end=",")
print()
for elem in b:
    print(elem, end=" ")