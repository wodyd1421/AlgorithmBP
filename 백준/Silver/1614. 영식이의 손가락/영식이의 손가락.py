fn = int(input())
fc = int(input())
if fc % 2 == 0:
    if fn == 1:
        print(8 * fc)
    elif fn == 2:
        print(4 * fc + 1)
    elif fn == 3:
        print(4 * fc + 2)
    elif fn == 4:
        print(4 * fc + 3)
    elif fn == 5:
        print(8 * fc + 4)
else:
    if fn == 1:
        print(8 * fc)
    elif fn == 2:
        print(4 * fc + 1 + 2)
    elif fn == 3:
        print(4 * fc + 2)
    elif fn == 4:
        print(4 * fc + 3 - 2)
    elif fn == 5:
        print(8 * fc + 4)