def permWithRepetition(s, r):
    result = []

    def backtrack(path):
        if len(path) == r:
            result.append(''.join(path))
            return
        for c in s:
            path.append(c)
            backtrack(path)
            path.pop()

    backtrack([])
    return result


s = input("enter the string: ")
r = int(input("enter the repetition number: "))

res = permWithRepetition(s, r)
print(res)
