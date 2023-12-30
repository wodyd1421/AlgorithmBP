def solution(myString):
    s = sorted(myString.split('x'))
    t = s[:]
    for l in t:
        if l == '':
            s.remove(l)
    return s