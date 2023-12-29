def solution(num_list):
    num1 = ''
    num2 = ''
    for n in num_list:
        if n % 2 != 1:
            num1 += str(n)
        else:
            num2 += str(n)
    return int(num1) + int(num2)