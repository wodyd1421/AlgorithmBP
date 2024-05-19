import math
n = int(input())
noc = 0
for i in range(n // 2 + 1):
    noc += math.comb(n - i, i)
print(noc % 10007)