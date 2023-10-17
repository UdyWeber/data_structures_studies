def insertion_sort(list_to_sort: list[int]):
    for i in range(1, len(list_to_sort)):
        temp = list_to_sort[i]
        j = i - 1

        while temp < list_to_sort[j] and j > -1:
            list_to_sort[j + 1] = list_to_sort[j]
            list_to_sort[j] = temp
            j -= 1

    return list_to_sort


if __name__ == '__main__':
    print(insertion_sort([1, 53, 23, 65, 99, 2, 12]))
