def solution(numbers, n):
    sum = 0
    for c in numbers:
        sum += c
        if sum > n:
            return sum