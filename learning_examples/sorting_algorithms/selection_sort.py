def selection_sort(list_to_sort: list[int]):
    for i in range(len(list_to_sort) - 1):
        min_index = i

        for j in range(min_index + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j

        if min_index != i:
            list_to_sort[min_index], list_to_sort[i] = list_to_sort[i], list_to_sort[min_index]

    return list_to_sort


if __name__ == "__main__":
    print(selection_sort([1, 53, 23, 65, 99, 2, 12]))
