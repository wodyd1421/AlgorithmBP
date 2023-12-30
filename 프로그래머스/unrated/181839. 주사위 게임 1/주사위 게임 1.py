def solution(a, b):
    if a * b % 2:
        ans = a ** 2 + b ** 2
    elif (a % 2 and not b % 2) or (not a % 2 and b % 2):
        ans = 2 * (a + b)
    else:
        ans = abs(a - b)
    return ans