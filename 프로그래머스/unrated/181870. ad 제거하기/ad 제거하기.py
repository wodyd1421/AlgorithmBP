def solution(strArr):
    result = []
    for word in strArr:
        if word.find('ad') == -1:
            result.append(word)
    return result