def solution(intStrs, k, s, l):
    answer = []
    for m in intStrs:
        if int(m[s:s+l]) > k:
            answer.append(int(m[s:s+l]))
    return answer