def countRepeatedChars(s):
    mp = {}
    for c in s:
        if c in mp:
            mp[c] += 1
        else:
            mp[c] = 1;
    for c in mp:
        print(f"{c} {mp[c]}")


myString = input("enter your string: ")
countRepeatedChars(myString)