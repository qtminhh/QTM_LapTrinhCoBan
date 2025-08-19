def swapCommasDots(s):
    s = s.replace(",", "#")
    s = s.replace(".", ",")
    s = s.replace("#", ".")
    return s;

myString = input("enter your string: ")
print(swapCommasDots(myString))