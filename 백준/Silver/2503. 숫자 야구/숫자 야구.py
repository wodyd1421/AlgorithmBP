arr = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i != j) and (j != k) and (k != i):
                arr.append(str(100*i+10*j+k))
n = int(input())
hints = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for tarstr in arr:
    ct = 0
    for targetp, strikep, ballp in hints:
        strike = 0
        ball = 0
        A = tarstr[0]
        B = tarstr[1]
        C = tarstr[2]
        a = str(targetp)[0]
        b = str(targetp)[1]
        c = str(targetp)[2]
        if A == a:
            strike += 1
        if B == b:
            strike += 1
        if C == c:
            strike += 1
        if (A == b) or (A == c):
            ball += 1
        if (B == a) or (B == c):
            ball += 1
        if (C == a) or (C == b):
            ball += 1
        if (strike == strikep) and (ball == ballp):
            ct += 1
        else:
            break
    if ct == n:
        ans += 1   
print(ans)