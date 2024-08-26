# Problem 6: Defendiendo la militancia
pdi = set()
pdc = set()
pdd = set()
while True:
    N = tuple(input().split())
    if N[0] == '#':
        break
    if N[1] == 'pdi':
        pdi.add(int(N[0]))
    elif N[1] == 'pdc':
        pdc.add(int(N[0]))
    else:
        pdd.add(int(N[0]))
trpl = pdi & pdc & pdd
dbl =  ((pdi & pdc) | (pdc & pdd) | (pdi & pdd)) - trpl
sngl = (pdi | pdc | pdd) - (trpl | dbl)
print(len(sngl), len(dbl), len(trpl))