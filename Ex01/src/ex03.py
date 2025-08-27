myString = input("enter your string: ")
if len(myString >= 2):
    print(myString[:2] + myString[-2:])
else:
    print("empty string")
