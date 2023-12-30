def solution(strArr):
    for i in range(len(strArr)):
        if not i % 2:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr