# Problem 3: Premiacion del Curso
gan = tuple([set(),set(),set(),set(),set()])
for i in range(5):
    for j in range(int(input())):
        gan[i].add(int(input()))
gan_tod = gan[0] & gan[1] & gan[2] & gan[3] & gan[4]
if gan_tod:
    print(1000000 // len(gan_tod))
else:
    print("Nadie gana")