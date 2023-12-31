def solution(k, d):
    count = 0
    index = 0
    for i in range(d // k, -1, -1):
        for j in range(index, d // k + 1):
            if (i * k) ** 2 + (j * k) ** 2 > d ** 2:
                index = j - 1
                count += j
                break
            elif j == d // k:
                count += j + 1
    return count