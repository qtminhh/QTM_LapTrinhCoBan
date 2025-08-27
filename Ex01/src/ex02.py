myString = input("enter your string: ")
freq = {}
for i in myString:
    freq[i] = freq.get(i, 0) + 1
print(freq)