def solution(arr, queries):
    b=[]
    for m in queries:
        a=[]
        for n in range(m[0],m[1]+1):
            if arr[n]>m[2]:
                a.append(arr[n])
        if a !=[]:
            b.append(min(a))
        else:
            b.append(-1)
    return b