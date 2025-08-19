def firstThree(string):
    if (len(string) < 3):
        return string
    return string[:3]


myString = input("enter your string: ")
print(firstThree(myString))
