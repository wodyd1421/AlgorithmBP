def solution(l, r):
    a=[]
    for n in range(l,r+1):
        if set(str(n)) in [{'0'},{'5'},{'0','5'}]:
            a.append(n)
    a.sort()
    if a==[]:
        a.append(-1)
    return a