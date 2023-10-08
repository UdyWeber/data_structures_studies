class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size
        self.idx = 0

    def __iter__(self):
        return self

    # Tried to implement my first generator :D
    def __next__(self):
        items = self.items()

        if self.idx < len(items):
            x = items[self.idx]
            self.idx += 1

            return x
        else:
            self.idx = 0
            raise StopIteration

    def __hash(self, key) -> int:
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def set_item(self, key, value):
        hashed_key = self.__hash(key)

        if self.data_map[hashed_key] is None:
            self.data_map[hashed_key] = [[key, value]]
        else:
            address_values = self.data_map[hashed_key]

            updated = False

            for address_value in address_values:
                if address_value[0] == key:
                    address_value[1] = value
                    updated = True
                    break

            if not updated:
                address_values.append([key, value])

    def get_item(self, key):
        hashed_key = self.__hash(key)
        address_values = self.data_map[hashed_key]

        if address_values is None:
            return None

        for value in address_values:
            if value[0] == key:
                return value[1]

        return None

    def keys(self) -> list[str]:
        keys_list = []

        for data_index in self.data_map:
            if data_index is None:
                continue

            for key_value_pairs in data_index:
                keys_list.append(key_value_pairs[0])

        return keys_list

    def items(self):
        items = []

        for data_index in self.data_map:
            if data_index is None:
                continue

            for key_value_pair in data_index:
                items.append((key_value_pair[0], key_value_pair[1]))

        return items

    def print_hashtable(self):
        for index, value in enumerate(self.data_map):
            print(f"{index}: {value}")


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


if __name__ == '__main__':
    h = HashTable()
    h.set_item('foo', 'bar')
    h.set_item('djabo', 'aham')
    h.set_item('jesus', "foo")
    h.print_hashtable()

    print(f"Keys of the hashtable: {h.keys()}")
    print(f"Value for djabo: {h.get_item('djabo')}")
    print(f"Value for djamba: {h.get_item('djamba')}")
