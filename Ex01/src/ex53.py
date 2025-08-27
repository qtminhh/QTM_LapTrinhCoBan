def firstRepeatedChar(s):
    charsDict = {}
    for c in s:
        if c not in charsDict:
            charsDict[c] = 1
        else:
            charsDict[c] += 1

    for c in s:
        if charsDict[c] == 2:
            return c

    return None


myString = input("enter your string: ")
print(firstRepeatedChar(myString))
