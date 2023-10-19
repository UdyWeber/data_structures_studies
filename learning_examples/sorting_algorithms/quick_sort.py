def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def pivot(x: list[int], pivot_index, end_index) -> int:
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if x[i] < x[pivot_index]:
            swap_index += 1
            swap(x, i, swap_index)

    swap(x, swap_index, pivot_index)
    return swap_index


def quick_sort_helper(list_to_sort: list[int], left_index, right_index):
    if left_index < right_index:
        pivot_index = pivot(list_to_sort, left_index, right_index)
        quick_sort_helper(list_to_sort, left_index, pivot_index - 1)
        quick_sort_helper(list_to_sort, pivot_index + 1, right_index)
    return list_to_sort


def quick_sort(list_to_sort: list[int]):
    return quick_sort_helper(list_to_sort, 0, len(list_to_sort) - 1)


if __name__ == '__main__':
    z = [4, 6, 1, 7, 3, 2, 5]
    print(quick_sort(z))
    print(remove_element([1, 1, 1, 1, 1], 1))

