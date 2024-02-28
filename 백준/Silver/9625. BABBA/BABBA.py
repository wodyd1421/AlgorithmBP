k = int(input())
a = [1] * (k+1)
b = [0] * (k+1)
for i in range(k):
    a[i+1] = b[i]
    b[i+1] = a[i] + b[i]
print(a[k], b[k])