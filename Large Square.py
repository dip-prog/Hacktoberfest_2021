import math
for _ in range(int(input())):
    n, l = map(int, input().split())
    print(math.floor(math.sqrt(n))*l)
