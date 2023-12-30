def solution(myString):
    ans = ''
    for x in myString:
        if ord(x) < ord('l'):
            ans += 'l'
        else:
            ans += x
    return ans
        