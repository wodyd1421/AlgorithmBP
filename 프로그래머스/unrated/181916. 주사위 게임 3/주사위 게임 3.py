def solution(a, b, c, d):
    e=[a,b,c,d]
    f=set(e)
    j=list(f)
    if len(f)==1:
        return 1111*a
    elif set([e.count(j[0]),e.count(j[1])]) == set([1,3]):
        if e.count(j[0])==3:
            return (10*j[0]+j[1])**2
        else:
            return (10*j[1]+j[0])**2
    elif set([e.count(j[0]),e.count(j[1])]) == set([2]):
        return (j[0]+j[1])*abs(j[0]-j[1])
    elif set([e.count(j[0]),e.count(j[1]),e.count(j[2])]) == set([1,2]):
        g=[e.count(j[0]),e.count(j[1]),e.count(j[2])]
        h=g.index(2)
        return a*b*c*d/j[h]**2
    else:
        return min(e)