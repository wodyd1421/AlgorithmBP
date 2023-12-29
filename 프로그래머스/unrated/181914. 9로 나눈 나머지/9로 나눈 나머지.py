def solution(number):
    answer = 0
    for m in number:
        answer += int(m)
    return answer%9