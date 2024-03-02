def check(arr, tar, low, high):
    mid = (low+high)//2
    if (low==high) and (arr[mid]!=tar):
        return 0
    if arr[mid] < tar:
        low = mid + 1
        return check(arr, tar, low, high)
    elif arr[mid] > tar:
        high = mid
        return check(arr, tar, low, high)
    else:
        return 1
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
low = 0
high = n - 1
m = int(input())
cl = list(map(int, input().split()))
for i in range(m):
    print(check(arr, cl[i], low, high), end=' ')