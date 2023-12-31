from itertools import permutations
import math
def solution(numbers):
    answer = 0
    a = []
    for i in range(1, len(numbers) + 1):
        a += permutations(numbers, i)
    b = []
    for i in a:
        b.append(int(''.join(i)))
    c = list(set(b))
    for i in c:
        k = 2
        while k <= math.sqrt(i):
            if i % k == 0:
                break
            if k + 1 > math.sqrt(i):
                answer += 1
                break
            k += 1
        if i in [2, 3]:
            answer += 1
    return answer