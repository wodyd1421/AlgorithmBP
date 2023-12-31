def solution(phone_book):
    a = sorted(phone_book)
    for i in range(len(a)-1):
        if a[i] == a[i+1][:len(a[i])]:
            return False
    return True