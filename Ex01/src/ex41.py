def stripChars(string, chars):
    return "".join(c for c in string if c not in chars)

myString = input("enter your string: ")
strippedChars = input("enter your set of characters to be strip: ")

print(stripChars(myString, strippedChars))