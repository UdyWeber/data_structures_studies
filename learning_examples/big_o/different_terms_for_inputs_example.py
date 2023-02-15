def print_items(number_of_items_a: int, number_of_items_b):
    for outer_number in range(number_of_items_a):
        for inner_number in range(number_of_items_b):
            print(outer_number, inner_number)


if __name__ == '__main__':
    print_items(
        number_of_items_a=10,
        number_of_items_b=20
    )


# So we have to take care when talking about different inputs cause different from our previous simplifications
# They matter here... So we have a function that takes 2 parameters a, b we would want to simplify this as O(n)
# Because the first for loop is O(n) the second too, so we have O(2n) simplified it will be O(n), but in this case
# That's incorrect cause the n in question could be different from the other, `a != b` so we only can simplify this as
# O(a + b)
