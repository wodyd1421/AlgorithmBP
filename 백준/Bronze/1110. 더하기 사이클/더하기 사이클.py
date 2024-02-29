n = input()
if len(n) == 1:
    n = '0' + n
m = n
count = 0
while True:
    m = m[1] + str(int(m[0])+int(m[1]))[-1]
    count += 1
    if m == n:
        print(count)
        break