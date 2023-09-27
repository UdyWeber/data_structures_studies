class HashTable:
    def __init__(self, size: int = 7):
        self.data_map = [None] * size

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

    def print_hashtable(self):
        for index, value in enumerate(self.data_map):
            print(f"{index}: {value}")


if __name__ == '__main__':
    h = HashTable()
    h.set_item('foo', 'bar')
    h.set_item('djabo', 'aham')
    h.set_item('jesus', "foo")
    h.print_hashtable()

    print(f"Value for djabo: {h.get_item('djabo')}")
    print(f"Value for djamba: {h.get_item('djamba')}")
