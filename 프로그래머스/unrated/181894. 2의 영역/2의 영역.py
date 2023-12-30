def solution(arr):
    if arr[-1] == 2:
        return arr[arr.index(2):]
    elif 2 in arr:
        return arr[arr.index(2):-arr[::-1].index(2)]
    else:    
        return [-1]