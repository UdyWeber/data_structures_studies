def print_items(number_of_items: int):
    for number in range(number_of_items):
        print(number)

    for _number in range(number_of_items):
        print(_number)


if __name__ == '__main__':
    print_items(10)


# This would be a pretty example of an n + n
# In this example we got 20 items printed out because we are adding 10 from the first loop to 10 from the second loop
# Mathematically speaking 2n. Or in our case O(2n) but we can simplify this by dropping the constant value O(n)
