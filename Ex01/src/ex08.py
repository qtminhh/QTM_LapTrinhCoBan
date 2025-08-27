myString = input("enter your string: ")
wordList = myString.split(" ")
maxLength = 0
longestWord = wordList[0]
for w in wordList:
    if (len(longestWord) < len(w)):
        longestWord = w
        maxLength = len(w)
print("longest word:", longestWord)
print("length of the longest word:", maxLength)