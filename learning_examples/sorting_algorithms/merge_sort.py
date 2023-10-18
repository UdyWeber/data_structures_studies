def merge(list_one: list[int], list_two: list[int]) -> list[int]:
    new_list = []
    i = 0
    j = 0

    # Zip the two lists until one is "empty"
    while i < len(list_one) and j < len(list_two):

        # As we add the value we increment the index on the list where the value
        # was appended to the new combined list
        if list_one[i] <= list_two[j]:
            new_list.append(list_one[i])
            i += 1
        else:
            new_list.append(list_two[j])
            j += 1

    # For the remaining items which were not added to the list
    # we append them on the end of the list, just iterating over the remaining indexes
    for value in list_one[i:]:
        new_list.append(value)

    for value in list_two[j:]:
        new_list.append(value)

    return new_list


# It's going to be recursive
def merge_sort(unsorted_list: list[int]):
    if len(unsorted_list) == 1:
        return unsorted_list

    mid_index = int(len(unsorted_list) / 2)

    left = merge_sort(unsorted_list[:mid_index])
    right = merge_sort(unsorted_list[mid_index:])

    return merge(left, right)


if __name__ == '__main__':
    print(merge_sort([5, 2, 56, 91, 3, 1]))
