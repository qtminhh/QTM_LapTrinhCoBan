def containsAllAlphabet(s):
    letters = set(ch.lower() for ch in s if ch.isalpha())
    return len(letters) == 26

myString = input("enter your string: ")
if (containsAllAlphabet(myString)):
    print("YES")
else:
    print("NO")