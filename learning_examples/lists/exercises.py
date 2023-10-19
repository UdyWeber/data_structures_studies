def remove_element(list_to_remove: list[int], value_to_remove: int) -> int:
    # Have to remove items backwards because of list resizing
    for i in range(len(list_to_remove), 0, -1):
        if list_to_remove[i - 1] == value_to_remove:
            list_to_remove.pop(i - 1)

    return len(list_to_remove)


def find_max_min(list_to_find: list[int]) -> tuple[int, int]:
    max_val = min_val = list_to_find[0]

    for value in list_to_find[1:]:
        if value > max_val:
            max_val = value
        if value < min_val:
            min_val = value

    return max_val, min_val


def find_longest_string(strings: list[str]) -> str:
    if not strings:
        return ""

    longest = strings[0]

    for value in strings[1:]:
        if len(longest) < len(value):
            longest = value

    return longest


def remove_duplicates(nums):
    if not nums:
        return 0

    write_pointer = 1

    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1

    return write_pointer


def max_profit(prices: list[int]) -> int:
    max_profit = 0

    if not prices:
        return max_profit

    for i in range(len(prices) - 1):
        yesterday_price = prices[i]

        for price in prices[i:]:
            today_profit = price - yesterday_price

            if today_profit > max_profit:
                max_profit = today_profit

    return max_profit


def rotate(nums: list[int], times: int):
    for _ in range(times, 0, -1):
        nums.insert(0, nums.pop())


def max_subarray(arr: list[int]):
    if not arr:
        return 0

    max_sum = current_sum = arr[0]

    for value in arr[1:]:
        current_sum = max(value, current_sum + value)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    print(remove_element([1, 1, 1, 1, 1], 1))
    print(find_max_min([4, 6, 1, 7, 3, 2, 5]))
    z = [1, 2, 3, 4, 5]
    rotate(z, 4)
    print(z)
    print(find_longest_string(['apple', 'banana', 'kiwi', 'pear']))
