def lastPartBefore(string, char):
    stringSplit = string.split(char)
    return stringSplit[0]
myString = input("enter your string: ")


specifiedChar = input("enter your specified character to split: ")
print(lastPartBefore(myString, specifiedChar))