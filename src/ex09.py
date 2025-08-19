myString = input("enter your string:")
if (len(myString) != 0):
    n = int(input("enter the index you want to remove:"))
    myString = myString[0:n] + myString[n + 1:]
    print(myString)
else:
    print("the string is empty!")
