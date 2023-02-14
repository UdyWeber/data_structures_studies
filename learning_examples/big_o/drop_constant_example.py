def print_items(number_of_items: int):
    for number in range(number_of_items):
        print(number)

    for _number in range(number_of_items):
        print(_number)


if __name__ == '__main__':
    print_items(10)


# This would be a pretty example of am n + n
# In this example we got 20 items printed out and twice as operations as the other
# Or mathematically speaking 2n or in our case O(2n) but we can simplify this by dropping the constant value
# So this example still a O(n) operation
