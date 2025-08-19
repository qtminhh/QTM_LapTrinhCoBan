def myReverse(string):
    if (len(string) % 4 == 0):
        return string[::-1]
    return "your string's length is not a multiple of 4"


myString = input("enter your string: ")
print(myReverse(myString))