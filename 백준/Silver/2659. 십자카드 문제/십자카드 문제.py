cn = []
for i in range(1111, 10000):
    if '0' in str(i):
        continue
    a = str(i)[0] + str(i)[1] + str(i)[2] + str(i)[3]
    b = str(i)[1] + str(i)[2] + str(i)[3] + str(i)[0]
    c = str(i)[2] + str(i)[3] + str(i)[0] + str(i)[1]
    d = str(i)[3] + str(i)[0] + str(i)[1] + str(i)[2]
    x = sorted([a, b, c, d])[0]
    if x not in cn:
        cn.append(x)
i = ''.join(input().split())
a = str(i)[0] + str(i)[1] + str(i)[2] + str(i)[3]
b = str(i)[1] + str(i)[2] + str(i)[3] + str(i)[0]
c = str(i)[2] + str(i)[3] + str(i)[0] + str(i)[1]
d = str(i)[3] + str(i)[0] + str(i)[1] + str(i)[2]
x = sorted([a, b, c, d])[0]
print(cn.index(x) + 1)