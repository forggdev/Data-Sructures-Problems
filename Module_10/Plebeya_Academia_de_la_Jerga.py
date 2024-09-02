# Problem 4: Plebeya Academia de la Jerga
dicc = {}
while True:
    N = input()
    if N == '#':
        break
    dicc[N] = N
for word in dicc:
    for i in range(1, len(word)-1):
        if word[:i] in dicc and word[i:] in dicc:
            print(word, "=", word[:i], '+', word[i:])

