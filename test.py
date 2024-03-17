import heapq as hpq
H = []
# hpq.heappush(H,2)
# hpq.heappush(H,74)
# hpq.heappush(H,55)
# hpq.heappush(H,10)
hpq.heappush(H,(10,2,3))
hpq.heappush(H,(2,4,6))
hpq.heappush(H,(6,9,8))
hpq.heappush(H,(5,2,3))
print(hpq.heappop(H))
