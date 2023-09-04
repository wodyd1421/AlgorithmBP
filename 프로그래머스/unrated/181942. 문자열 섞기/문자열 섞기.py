def solution(str1, str2):
    answer = []
    for i in range(2 * len(str1)):
        if i % 2 == 0:
            answer.append(str1[int(i / 2)])
        else:
            answer.append(str2[int((i-1) / 2)])
    answer = ''.join(answer)
    return answer