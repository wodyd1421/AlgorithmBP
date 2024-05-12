ct = [[0, 0] for _ in range(41)]
ct[0][0] += 1
ct[1][1] += 1
for i in range(2, 41):
    ct[i][0] = ct[i-1][0] + ct[i-2][0]
    ct[i][1] = ct[i-1][1] + ct[i-2][1]
t = int(input())
for _ in range(t):
    n = int(input())
    print(ct[n][0], ct[n][1])