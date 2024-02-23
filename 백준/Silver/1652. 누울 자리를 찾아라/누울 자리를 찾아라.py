n = int(input())
arr = []
ctx = 0
cty = 0
for _ in range(n):
    x = str(input())
    arr.append(x)
    check = 0
    for i in range(n):
        if x[i] == '.':
            check += 1
            if check == 2:
                ctx += 1
        else:
            check = 0
for i in range(n):
    check = 0
    for j in range(n):
        if arr[j][i] == '.':
            check += 1
            if check == 2:
                cty += 1
        else:
            check = 0
print(ctx, cty)