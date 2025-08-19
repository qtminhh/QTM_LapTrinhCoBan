myString = input("enter your string: ")
firstChar = myString[0]
myString = myString.replace(firstChar, '$')
myString = firstChar + myString[1:]
print(myString)