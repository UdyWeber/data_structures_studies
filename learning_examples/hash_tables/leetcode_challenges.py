# Interview Question: Return if the lists have a value in common
def inefficient_list_comparator(list_one: list, list_two: list):
    # This is O(n^2) cause you will have to iterate over and over both lists
    for i in list_one:
        for k in list_two:
            if i == k:
                return True
    return False


def efficient_list_comparator(list_one: list, list_two: list):
    table = {}

    # First we put the list into a dictionary that's O(n) cause indexing and item is O(1)
    for i in list_one:
        table[i] = True

    # Here its also O(n) cause when we hit the key if it's in the dictionary the function will return right away
    # So we will not have to iterate again and again over the values of the second list, we will just do it one time.
    for k in list_two:
        if k in table:
            return True

    # O(n) > O(n^2)

    return False


# Leet code exercise
# Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).

# My Solution
def mine_find_duplicates(nums: list[int]):
    table = {}
    duplicates = []

    for i in nums:
        if i in duplicates:
            continue
        elif i not in table:
            table[i] = True
        else:
            duplicates.append(i)

    return duplicates


# Example solution
def example_find_duplicates(nums: list[int]):
    table = {}

    for i in nums:
        table[i] = table.get(i, 0) + 1

    return [num for num in table if table[num] > 1]


# Solved by my self :D
def first_non_repeating_char(string_to_go_against: str):
    char_counts = {}

    for char in string_to_go_against:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in string_to_go_against:
        if char_counts[char] == 1:
            return char

    return None


# leetcode challenge
# Needed example to solve :(
def group_anagrams(strings: list[str]) -> list[list[str]]:
    anagrams = {}

    for i in strings:
        # Transform string in a key of the sorted anagram cause anagrams will have the exact same key
        common = "".join(sorted(i))

        if common not in anagrams:
            anagrams[common] = [i]
        else:
            anagrams[common].append(i)

    return list(anagrams.values())


# leetcode challenge
# Solved by my self :D
def two_sum(nums: list[int], target: int) -> list[int]:
    indexes = {}

    for index, i in enumerate(nums):
        diff = target - i

        if diff in indexes:
            return [indexes[diff], index]

        indexes[i] = index

    return []


# leetcode challenge (Hard)
# Needed example to solve :(
def subarray_sum(nums: list[int], target: int) -> list[int]:
    # Store where the sum happened in list
    sum_index = {0: -1}

    # Sum value to keep track
    current_sum = 0

    for index, value in enumerate(nums):
        current_sum += value
        # Check if the sum has happened before in list
        diff = current_sum - target

        if diff in sum_index:
            # If it has happened before get the path by the sum key and get the index where it occurred
            starting_index = sum_index[diff] + 1
            return [starting_index, index]

        # Else update the sum index
        sum_index[current_sum] = index

    return []


# Without using the set() function
def remove_duplicates(nums: list[int]) -> list[int]:
    uniques = {}

    for num in nums:
        if num in uniques:
            continue
        else:
            uniques[num] = None

    return list(uniques.keys())


# Using the set() function
def remove_duplicates_with_set(nums: list[int]) -> list[int]:
    return list(set(nums))


def has_unique_chars(string: str):
    char_set = set()

    for char in string:
        if char in char_set:
            return False
        char_set.add(char)

    return True


def find_pairs(list1: list[int], list2: list[int], target: int) -> list[tuple[int, int]]:
    possible_matchs = set(list1)
    pairs = []

    for j in list2:
        diff = target - j

        if diff in possible_matchs:
            pairs.append((diff, j))

    return pairs


# Needed Example to complete understand
# Without example 8 of 9 tests passed
def longest_consecutive_sequence(nums: list[int]):
    longest_sequence = 0
    nums_set = set(nums)

    for num in nums:
        # Means that the num we are in is the start of a sequence
        if num - 1 not in nums_set:
            current_sequence = 1

            # Need to do this because we will iterate using the number and updating it
            current_num = num

            while current_num + 1 in nums_set:
                current_sequence += 1
                current_num += + 1

            if current_sequence > longest_sequence:
                longest_sequence = current_sequence

    return longest_sequence


if __name__ == '__main__':
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

    print(find_pairs([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], 7))

    print(has_unique_chars('abcLd#efg'))

    print(first_non_repeating_char("leetcode"))
    print(first_non_repeating_char('hello'))
    print(first_non_repeating_char('aabbcc'))

    print(two_sum([5, 1, 7, 2, 9, 3], 10))
    print(two_sum([4, 2, 11, 7, 6, 3], 9))
    print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
    print(two_sum([1, 3, 5, 7, 9], 10))
    print(two_sum([1, 2, 3, 4, 5], 10))
    print(two_sum([1, 2, 3, 4, 5], 7))
    print(two_sum([1, 2, 3, 4, 5], 3))
    print(two_sum([], 0))

    print(subarray_sum([1, 2, 3, 4, 5], 9))

    print("1st set:")
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
