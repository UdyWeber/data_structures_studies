def check_space_in_memory_for_dictionaries():
    dict_one = {"value": 11}
    dict_two = dict_one

    print("Value of dict_one: ", dict_one)
    print("Value of dict_two: ", dict_two)

    print("\nValues before Update")
    print("Id of memory dict_one: ", id(dict_one))
    print("Id of memory dict_two: ", id(dict_two))

    dict_two['value'] = 22

    print("\nValue of num_one: ", dict_one)
    print("Value of dict_two: ", dict_two)

    print("\nValues after Update")
    print("Id of memory dict_one: ", id(dict_one))
    print("Id of memory dict_two: ", id(dict_two))

    dict_three = {"value": 33}
    dict_two = dict_three

    print("\nValues after Update two to three")
    print("Value of num_one: ", dict_one)
    print("Value of dict_two: ", dict_two)
    print("Value of dict_three: ", dict_three)

    print("\nValues after Update")
    print("Id of memory dict_one: ", id(dict_one))
    print("Id of memory dict_two: ", id(dict_two))
    print("Id of memory dict_three: ", id(dict_three))

    dict_one = dict_three

    print("\nValues after Update one to three")
    print("Value of num_one: ", dict_one)
    print("Value of dict_two: ", dict_two)
    print("Value of dict_three: ", dict_three)

    print("\nValues after Update")
    print("Id of memory dict_one: ", id(dict_one))
    print("Id of memory dict_two: ", id(dict_two))
    print("Id of memory dict_three: ", id(dict_three))


if __name__ == "__main__":
    check_space_in_memory_for_dictionaries()

# As we can see the output were different from the inter pointers example cause dictionaries instead of integers
# Are mutable in memory and dict_one and dict_two point to the same space on memory, so when dict_two is updated
# Dict one also changes cause both are the same
# With dicts we can repoint it to another space in memory as we do when we point dict_two that as point to dict_one
# To dict_three so three and two are pointing to the same space now
# And if we point one to three all the dictionaries are pointed for the same space in memory
# And the items in memory that has no pointers pointing to it
# are collected by python garbage collector and removed from memory
