def add_items(number: int) -> int:
    return number + number + number


if __name__ == '__main__':
    print(add_items(1))


# So in this example we are performing ONE single operation in our function
# On the previous examples we were observing that as the N (our input) was increasing the number of operations were too
# But in this case our number of N doesn't matter because it will be on single operation despite the value we pass in
# That's called a O(1) yoy may think that it could be a O(2) but no,
# cause the operation we are doing is constant we are constantly adding n + n + n + n...
