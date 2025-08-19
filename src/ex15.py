def addTags(tag, s):
    return f"<{tag}>{s}</{tag}>"

myString = input("enter your string: ")
htmlTag = input("enter your HTML tag: ")
print(addTags(htmlTag, myString))