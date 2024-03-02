# Problem 6
A = int(input())
for i in range(A):
    B = int(input())
    Tab = tuple(map(int, input().split()))
    indexes = ()
    movements = 0
    position = 0
    while True:
        movements += 1
        indexes += (position,)
        position += Tab[position]
        if position in indexes or position<0 or position>=len(Tab):
            break
    print(movements)