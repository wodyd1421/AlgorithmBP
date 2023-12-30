def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            del stk[-1]
        else:
            stk.append(arr[i])
    return stk if stk else [-1]