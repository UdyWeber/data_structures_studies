my_list = [12, 53, 6, 8, 91]

# This is my list, that has 5 items if we want to add or remove an item that's in the end
# We use the append() method to add it to the end and the pop() method to remove
# Both of these methods are O(1) because we only have to do one operation at the end of the list
# Same as searching for a value in a list if we know the index we go directly to it so its O(n)

my_list.insert(1, "Hello World")

# As we perform the insert method, we are pushing a value into the index 1 that's being occupied by 53
# So as we have our new index 1 all the indexes that come after 1 will be updated it will be index + 1 for every
# Item in the list that comes after the index 1, so it is considered O(n) n being the number of items
# The same for the pop method when specified an index, it will remove tha value that's in the index and all the ones that
# Come after it will be updated index - 1

my_list.pop(4)

if __name__ == "__main__":
    print(my_list)

