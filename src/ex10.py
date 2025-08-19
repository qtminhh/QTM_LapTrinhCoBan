myString = input("enter your string:")
myString = myString[-1] + myString[1:-1] + myString[0]
print(myString)