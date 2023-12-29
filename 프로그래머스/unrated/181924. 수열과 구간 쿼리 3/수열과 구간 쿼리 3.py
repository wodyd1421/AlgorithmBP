def solution(arr, queries):
    for m in queries:
        temp=arr[m[0]]
        arr[m[0]]=arr[m[1]]
        arr[m[1]]=temp
    return arr