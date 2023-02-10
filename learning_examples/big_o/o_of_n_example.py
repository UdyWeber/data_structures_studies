def print_items(number_of_items: int):
    for number in range(number_of_items):
        print(number)


if __name__ == '__main__':
    print_items(10)

# This is the O(n) example
# So print_items is a function that iterates over a range of numbers and print each number in this range
# It is a O(n) because we are passing to it the number of operations it has to make to achieve its purpose
# And by that the number of operations will be proportional to the number of the input we passed in
# If we put it in a graphic y-axis being the O and n being the x-axis, we could see that it would make a straight line
