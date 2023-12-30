def solution(arr, idx):
    if 1 in arr[idx:]:
        return idx + arr[idx:].index(1)
    else:
        return -1