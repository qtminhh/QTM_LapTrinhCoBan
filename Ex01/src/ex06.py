myString = input("enter your string: ")
if (len(myString) < 3):
    print(myString)
else:
    if (myString[-3:] == "ing"):
        print(myString + "ly")
    else:
        print(myString + "ing")