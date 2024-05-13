n = int(input())
arr = [0] * (10**6+1)
for i in range(1, 10**6+1):
    if i * 3 <= 10 ** 6:
        arr[i*3] = arr[i]+1
    if i * 2 <= 10 ** 6:
        if arr[i*2] == 0:
            arr[i*2] = arr[i] + 1
        else:
            arr[i*2] = min(arr[i]+1, arr[i*2])
    if i + 1 <= 10 ** 6:
        if arr[i+1] == 0:
            arr[i+1] = arr[i] + 1
        else:
            arr[i+1] = min(arr[i]+1, arr[i+1])
print(arr[n])