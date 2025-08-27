def splitOnLast(s, delimiter):
    parts = s.rsplit(delimiter, 1)
    return parts


myString = input("enter your string: ")
delimiter = input("enter your delimiter: ")
print(splitOnLast(myString, delimiter))
