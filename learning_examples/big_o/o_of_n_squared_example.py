def print_items(number_of_items: int):
    for outer_number in range(number_of_items):
        for inner_number in range(number_of_items):
            print(outer_number, inner_number)


if __name__ == '__main__':
    print_items(10)

# So this is an example of O(n^2) where we are running the same operation but nesting them at different levels
# The first for loop is in each iteration is calling the inner for loop to run and complete its cycle
# In order to the outer loop complete its cycle, so we are doing n * n operations
# The simplification for this example is that it doesn't matter how much nesting we will have
# It can be O(n^6) but we are simplifying it as O(n^2).
# That is the less efficient big O
