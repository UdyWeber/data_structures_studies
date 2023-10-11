from learning_examples.heap.MaxHeap import MaxHeap


def find_kth_smallest_using_list(nums, k):
    """Return the smallest kth value using normal list"""
    return sorted(nums)[k - 1]


def find_kth_smallest_using_heap(nums, k):
    """Return the smallest kth value using heap"""
    mh = MaxHeap()

    for i in nums:
        mh.insert(i)

        if len(mh.heap) > k:
            mh.remove()

    return mh.remove()


def stream_max_using_list(nums):
    max_values = []
    max_num = 0

    for idx, i in enumerate(nums):
        if idx == 0:
            max_num = i
        else:
            max_num = max(max_num, i)

        max_values.append(max_num)

    return max_values


def stream_max_using_heap(nums):
    mh = MaxHeap()
    max_values = []

    for i in nums:
        # Each time an element is added, if it is the greatest it is put at the top of the heap
        # So putting it at the top means that is the MAX value of the heap so far being the max value of the stream too
        mh.insert(i)
        max_values.append(mh.heap[0])

    return max_values


if __name__ == "__main__":
    assert find_kth_smallest_using_list([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 5
    assert find_kth_smallest_using_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 5
    assert stream_max_using_list([-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]
    assert stream_max_using_heap([-1, -2, -3, -4, -5]) == [-1, -1, -1, -1, -1]
