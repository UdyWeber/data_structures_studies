def swap(my_list, index_one, index_two):
    my_list[index_one], my_list[index_two] = my_list[index_two], my_list[index_one]


def less_optimized_bubble_sort(list_to_sort: list[int]):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - 1):
            if list_to_sort[i] < list_to_sort[j]:
                swap(list_to_sort, i, j)


def bubble_sort(list_to_sort: list[int]):
    # Goes through the list backwards
    for i in range(len(list_to_sort) - 1, 0, -1):
        # Goes through the list just in the range to do the comparisons
        # assuming that is already a little sorted we cut the operation by one
        for j in range(i):
            # We compare using J because J will be always small steps into the values
            if list_to_sort[j] > list_to_sort[j + 1]:
                swap(list_to_sort, j, j + 1)

    return list_to_sort


if __name__ == "__main__":
    print(bubble_sort([1, 53, 23, 65, 99, 2, 12]))

