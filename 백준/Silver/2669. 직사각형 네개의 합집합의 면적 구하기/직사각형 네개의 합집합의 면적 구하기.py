arr = [[0]*100 for x in range(100)]
ct = 0
for i in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(a,c):
        for k in range(b,d):
            if arr[j][k] == 0:
                arr[j][k] = 1
                ct += 1
print(ct)