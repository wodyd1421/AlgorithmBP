def solution(my_string, queries):
    a=list(my_string)
    for s,e in queries:
        if s == 0:
            a[:e+1]=a[e::-1]
        else:
            a[s:e+1]=a[e:s-1:-1]
    return ''.join(a)