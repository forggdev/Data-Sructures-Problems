# Problem 5: Conteo de Votos
Vot = {}
Cand = {}
while True:
    doc, candidato = map(int, input().split())
    if doc == 0 and candidato == 0:
        break
    if doc in Vot:
        if Vot[doc] == -1:
            continue
        else:
            Cand[Vot[doc]] -= 1
            if Cand[Vot[doc]] == 0:
                Cand.pop(Vot[doc])
            Vot[doc] = -1
    else:
        Vot[doc] = candidato
        if candidato in Cand:
            Cand[candidato] += 1
        else:
            Cand[candidato] = 1
Cand = sorted(Cand.items(), key=lambda x:  (x[1], x[0]), reverse=True)
for elem in Cand:
    print(elem[0], elem[1])