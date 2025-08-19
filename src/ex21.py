def convert(string):
    cnt = 0
    for char in string[:4]:
        if char.isupper():
            cnt += 1
    if cnt >= 2:
        return string.upper()
    return string

myString = input("enter your string: ")
print(convert(myString))