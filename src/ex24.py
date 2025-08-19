def startingCharsCheck(string, chars):
    if chars == string[:len(chars)]:
        return True
    return False


myString = input("enter your string: ")
startingChars = input("enter the starting characters: ")
if not startingCharsCheck(myString, startingChars):
    print("no, your string does not start with", startingChars)
else:
    print("yes, your string starts with", startingChars)