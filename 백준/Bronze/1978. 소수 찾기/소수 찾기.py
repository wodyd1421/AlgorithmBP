input()
tar = map(int, input().split())
prime = [0, 0] + [1] * 999
for i in range(2, 1001):
    if prime[i] == 1:
        for j in range(2*i, 1001, i):
            prime[j] = 0
ct = 0
for x in tar:
    if prime[x] == 1:
        ct += 1
print(ct)