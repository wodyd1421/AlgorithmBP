from bisect import bisect_left, bisect_right
def count_by_range(a, left, right):
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index - left_index
n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int, input().split()))
for x in arr2:
    print(count_by_range(arr1, x, x), end=' ')