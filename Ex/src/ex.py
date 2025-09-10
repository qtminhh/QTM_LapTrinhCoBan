# 1. Max of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 2. Sum of a list
def sum_list(nums):
    return sum(nums)

# 3. Reverse a string
def reverse_string(s):
    return s[::-1]

# 4. Factorial
def factorial(n):
    if n < 0: return None
    return 1 if n in (0, 1) else n * factorial(n - 1)

# 5. Prime check
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

# 6. Prime numbers
def primes_less_than_n():
    n = int(input("Enter a number: "))
    print([x for x in range(2, n) if is_prime(x)])

def first_n_primes(N):
    primes, num = [], 2
    while len(primes) < N:
        if is_prime(num): primes.append(num)
        num += 1
    print(primes)

# 7. Perfect numbers
def is_perfect(n):
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def perfects_under_1000():
    print([x for x in range(2, 1000) if is_perfect(x)])

# 8. Pangram
def is_pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())


# --- Demo ---
if __name__ == "__main__":
    print(max_of_three(10, 25, 15))
    print(sum_list([1, 2, 3, 4, 5]))
    print(reverse_string("hello"))
    print(factorial(5))
    print(is_prime(29))
    # primes_less_than_n()
    first_n_primes(10)
    perfects_under_1000()
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
