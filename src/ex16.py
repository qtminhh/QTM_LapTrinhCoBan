def insetStingMiddle(string1, string2):
    return string1[:len(string1)//2] + string2 + string1[len(string1)//2:]


myString1 = input("enter your first string: ")
myString2 = input("enter your second string: ")
print("insert the second string into the middle of the first string: ", insetStingMiddle(myString1, myString2))
