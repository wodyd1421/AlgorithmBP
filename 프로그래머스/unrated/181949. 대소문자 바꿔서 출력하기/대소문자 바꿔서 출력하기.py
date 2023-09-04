str = input()

list = list(str)
length = len(list)
for a in range(length):
    if list[a].isupper():
        list[a] = list[a].lower()
    else:
        list[a] = list[a].upper()
str = ''.join(list)
print(str)