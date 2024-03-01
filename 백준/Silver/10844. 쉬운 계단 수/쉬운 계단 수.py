n = int(input())
prev = [1] * 10
new = [0] * 10
for _ in range(n-1):
    new[0] = prev[1]
    for i in range(8):
        new[i+1] = prev[i] + prev[i+2]
    new[9] = prev[8]
    prev = new[:]
print(sum(prev[1:])%1000000000)