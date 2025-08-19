def toLowerFirstNChars(s, n):
    return s[:n].lower() + s[n:]


myString = input("enter your string: ")
n = int(input("enter the number of first characters you want to convert to lowercase: "))

print(toLowerFirstNChars(myString, n))
