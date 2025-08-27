def addZero(numList, width):
    for num in numList:
        print(str(num).zfill(width))


n = int(input("enter number of integers: "))
w = int(input("enter width: "))
nums = []
for i in range(n):
    nums.append(int(input(f"enter integer number {i+1}: ")))
addZero(nums, w)
