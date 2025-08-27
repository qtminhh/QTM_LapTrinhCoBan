def formattedNum(numList):
    for i in numList:
        print(round(i))


n = int(input("enter the number of numbers: "))
myNumList = []
for i in range(n):
    num = float(input(f"enter number {i+1}: "))
    myNumList.append(num)

formattedNum(myNumList)

