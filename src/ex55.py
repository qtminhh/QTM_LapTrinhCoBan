def firstRepeatedWord(s):
    words = s.split(" ")
    wordsDict = {}
    for w in words:
        if w not in wordsDict:
            wordsDict[w] = 1
        else:
            wordsDict[w] += 1

    for w in words:
        if wordsDict[w] == 2:
            return w

    return None


myString = input("enter your string: ")
print(firstRepeatedWord(myString))
