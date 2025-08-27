def notPoorReplace(s):
    notPos = s.find("not") #tra ve vi tri cua 'not'
    poorPos = s.find("poor") #tra ve vi tri cua 'poor'

    if notPos != -1 and poorPos != -1 and notPos < poorPos: #neu co ca not va poor va not dung truoc poor
        s = s[:notPos] + "good" + s[poorPos + 4:]  #vi len(poor)=4
    return s


myString = input("enter your string: ")
print(notPoorReplace(myString))