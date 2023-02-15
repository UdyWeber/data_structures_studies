def check_space_in_memory_for_integers():
    num_one = 11
    num_two = num_one

    print("Value of num_one: ", num_one)
    print("Value of num_two: ", num_two)

    print("\nValues before Update")
    print("Id of memory num_one: ", id(num_one))
    print("Id of memory num_two: ", id(num_two))

    num_two = 22

    print("\nValue of num_one: ", num_one)
    print("Value of num_two: ", num_two)

    print("\nValues after Update")
    print("Id of memory num_one: ", id(num_one))
    print("Id of memory num_two: ", id(num_two))


if __name__ == "__main__":
    check_space_in_memory_for_integers()

# Second we will point num_two to num_one
# First we will have our value created in memory 11, and we will point num_one to this value
# But the question still, will num_two point to the same space in memory that num_one
# Or will it create a new space in memory for a copy of the value of num_one
# So we can see in the example that both point to the same space in memory

# So if we override the value of num_two with 22 will it set the value of
# num_one to eleven or will it create a new space in memory for 22
# So we can see that 22 has been created a new space in memory
# That happen because integers are immutable in memory, you cannot change them.
