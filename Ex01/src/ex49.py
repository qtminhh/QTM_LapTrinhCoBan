def vowelsCount(s):
    vowels = {"a":0, "e":0, "i":0, "u":0, "o":0}
    for c in s:
        if c in vowels:
            vowels[c] += 1

    for c in vowels:
        if vowels[c] > 0:
            print(f"{c} {vowels[c]}")


myString = input("enter your string: ")
vowelsCount(myString)