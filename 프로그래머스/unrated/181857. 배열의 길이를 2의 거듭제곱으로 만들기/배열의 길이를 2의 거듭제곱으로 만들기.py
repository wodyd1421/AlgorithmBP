def solution(arr):
    if len(arr)==1:
        return arr
    for i in range(10):
        if 2 ** i < len(arr) <= 2 ** (i + 1):
            return arr+[0 for i in range(2**(i+1)-len(arr))]