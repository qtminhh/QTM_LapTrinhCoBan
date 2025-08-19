myString = input("enter your string: ")
words = myString.split(" ")
for i in range(len(words)):
    words[i] = words[i][::-1]
reversedWordString = " ".join(words)
print(reversedWordString)
