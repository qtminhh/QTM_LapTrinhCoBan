# 1. Sum all items in a list
def sum_list(lst):
    return sum(lst)

# 2.Multiply all items in a list
def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

# 3. Get the largest number from a list
def max_in_list(lst):
    return max(lst)

# 4. Get the smallest number from a list
def min_in_list(lst):
    return min(lst)

# 5. Count strings with length >=2 and same first and last char
def count_special_strings(lst):
    return sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])

# 6. Sort a list of tuples by the last element
def sort_by_last_element(lst):
    return sorted(lst, key=lambda x: x[-1])

# 7. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 8. Check if a list is empty
def is_list_empty(lst):
    return len(lst) == 0

# 9. Clone or copy a list
def clone_list(lst):
    return lst.copy()

# 10. List words longer than n
def words_longer_than(lst, n):
    return [word for word in lst if len(word) > n]

# 11. Check if two lists have at least one common member
def have_common_member(lst1, lst2):
    return bool(set(lst1) & set(lst2))

# 12. Remove 0th, 4th, 5th elements from a list
def remove_indices(lst, indices=[0,4,5]):
    return [v for i,v in enumerate(lst) if i not in indices]

# 13. Generate a 3*4*6 3D array of '*'
def generate_3d_array():
    return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

# 14. Remove even numbers from a list
def remove_even_numbers(lst):
    return [x for x in lst if x % 2 != 0]

# 15. Shuffle a list
import random
def shuffle_list(lst):
    temp = lst.copy()
    random.shuffle(temp)
    return temp

# 16. List of first and last 5 square numbers between 1 and 30
def first_last_squares():
    squares = [i**2 for i in range(1, 6)] + [i**2 for i in range(6, 31) if i**2 <= 30][-5:]
    return squares

# 17. Check if all numbers in a list are prime
def are_all_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    return all(is_prime(x) for x in lst)

# 18. Generate all permutations of a list
from itertools import permutations
def all_permutations(lst):
    return list(permutations(lst))

# 19. Difference between two lists
def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

# 20. Access index of a list
def list_indices(lst):
    return list(range(len(lst)))

# 21. Convert list of characters into string
def chars_to_string(lst):
    return ''.join(lst)

# 22. Find index of an item in list
def index_of_item(lst, item):
    return lst.index(item) if item in lst else -1

# 23. Flatten a shallow list
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

# 24. Append one list to another
def append_list(lst1, lst2):
    return lst1 + lst2

# 25. Select a random item from list
def random_item(lst):
    return random.choice(lst)

# 26. Check circularly identical lists
def are_circularly_identical(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    doubled = lst1 * 2
    for i in range(len(lst1)):
        if doubled[i:i+len(lst2)] == lst2:
            return True
    return False

# 27. Second smallest number in a list
def second_smallest(lst):
    unique_sorted = sorted(set(lst))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# 28. Second largest number in a list
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# 29. Get unique values from a list
def unique_values(lst):
    return list(set(lst))

# 30. Frequency of elements in a list
from collections import Counter
def frequency(lst):
    return dict(Counter(lst))

# 31. Count elements within a range
def count_in_range(lst, start, end):
    return sum(start <= x <= end for x in lst)

# 32. Check if a list contains a sublist
def contains_sublist(lst, sublst):
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False

# 33. Generate all sublists of a list
def all_sublists(lst):
    result = []
    for i in range(len(lst)+1):
        for j in range(i+1,len(lst)+1):
            result.append(lst[i:j])
    return result

# 34. Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    sieve = [True]*(n+1)
    sieve[0:2] = [False,False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# 35. Concatenate list with range
def concatenate_with_range(lst, n):
    return [f"{x}{i}" for i in range(1, n+1) for x in lst]

# 36. Get a variable with identification
def variable_id(var):
    return id(var)

# 37. Find common items in two lists
def common_items(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 38. Swap every n-th value with (n+1)th
def swap_every_second(lst):
    res = lst.copy()
    for i in range(0, len(lst)-1, 2):
        res[i], res[i+1] = res[i+1], res[i]
    return res

# 39. Convert list of integers into a single integer
def list_to_integer(lst):
    return int(''.join(map(str,lst)))

# 40. Split list based on first character
def split_by_first_char(lst):
    d = {}
    for word in lst:
        key = word[0]
        d.setdefault(key, []).append(word)
    return d

# 41. Create multiple lists
def create_multiple_lists(n, value=None):
    return [[value]*n for _ in range(n)]

# 42. Find missing and additional values in two lists
def missing_and_additional(lst1, lst2):
    set1, set2 = set(lst1), set(lst2)
    missing = list(set1 - set2)
    additional = list(set2 - set1)
    return missing, additional

# 43. Split a list into different variables
def split_list(lst):
    return tuple(lst)

# 44. Generate groups of five consecutive numbers in a list
def groups_of_five(lst):
    return [lst[i:i+5] for i in range(0,len(lst),5)]

# 45. Convert pair of values into sorted unique array
def sorted_unique_array(pair):
    return sorted(set(pair))

# 46. Select odd items from a list
def odd_items(lst):
    return [x for x in lst if x % 2 == 1]

# 47. Insert an element before each element of a list
def insert_before_each(lst, elem):
    res = []
    for x in lst:
        res.append(elem)
        res.append(x)
    return res

# 48. Print nested lists each on a new line
def print_nested_lists(nested):
    for sublist in nested:
        print(sublist)

# 49. Convert list to list of dictionaries
def lists_to_dicts(names, codes):
    return [{'color_name': n, 'color_code': c} for n, c in zip(names, codes)]

# 50. Sort a list of nested dictionaries
def sort_nested_dicts(lst, key_name):
    return sorted(lst, key=lambda x: x[key_name])
