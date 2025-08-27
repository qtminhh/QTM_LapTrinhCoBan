def aligned(num):
    s = str(num)
    print("left aligned:", s.ljust(10))
    print("right aligned:", s.rjust(10))
    print("center aligned:", s.center(10))


n = float(input("enter a number: "))
aligned(n)
