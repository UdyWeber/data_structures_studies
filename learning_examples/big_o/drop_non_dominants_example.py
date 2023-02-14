def print_items(number_of_items: int):
    for outer_number in range(number_of_items):
        for inner_number in range(number_of_items):
            print(outer_number, inner_number)

    for other_outer_number in range(number_of_items):
        print(other_outer_number)


if __name__ == '__main__':
    print_items(10)

# So here we have the same nested for loop `O(n^2)`, but we have another one below that does `O(n)`
# And we are trying to simplify the O notation, so here we are going to do the simplification by dropping
# The smaller part of the equation if we put this all together it will be O(n^2 + n) and thinking of N = 10
# So n will be 10 and n^2 will be 100, and what we have to do is cut the smaller part of it, so we simplify
# O(n^2 + n) in O(n^2) cause the n only represent 10% of n^2)
