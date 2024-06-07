def solution(price, money, count):
    sum = (1 + count) * count / 2
    needed = price * sum - money
    return max(0, needed)