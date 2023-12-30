def solution(strArr):
    arr =[0]*30
    for str in strArr:
        arr[len(str)-1] += 1
    return max(arr)