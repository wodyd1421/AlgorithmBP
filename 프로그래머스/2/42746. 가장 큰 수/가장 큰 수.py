def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = ''.join(sorted(numbers, key=lambda x: 3*x, reverse=True))
    if numbers[0] == '0': numbers = '0'
    return numbers