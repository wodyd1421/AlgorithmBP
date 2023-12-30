def solution(myString):
    preresult = myString.split('x')
    return list(map(len, preresult))