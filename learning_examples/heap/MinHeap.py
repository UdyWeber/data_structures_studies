class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index: int):
        return index * 2 + 1

    def _right_child(self, index: int):
        return index * 2 + 2

    def _parent(self, index: int):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        min_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # We have to make those if statements separately because the value must be put in the right order
            # We have to first check if the index exists in the list range
            if (left_index < len(self.heap)) and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index

            if (right_index < len(self.heap)) and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index

            # When the min index is reached it means we have to stop iterating cause all the values are correctly put
            if min_index != index:
                self._swap(min_index, index)
                index = min_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        index_of_value = len(self.heap) - 1

        while index_of_value > 0 and self.heap[index_of_value] < self.heap[self._parent(index_of_value)]:
            parent_index = self._parent(index_of_value)

            self._swap(index_of_value, parent_index)
            index_of_value = parent_index

    def remove(self):
        if not self.heap:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

    def print_heap(self):
        for i, value in enumerate(self.heap):
            if i == 0:
                print(f"Root: {value}")
            else:
                first_parent = parent_index = self._parent(i)
                path = [str(value)]

                while parent_index >= 0:
                    path.append(str(self.heap[parent_index]))
                    parent_index = self._parent(parent_index)

                tree_level = ((first_parent + 1) // 2) + 1
                print(f"[LEVEL {tree_level}] " + " -> ".join(path[::-1]))


if __name__ == "__main__":
    mh = MinHeap()
    mh.insert(23)
    mh.insert(123)
    mh.insert(12)
    mh.insert(1000)
    mh.insert(75)
    mh.insert(1500)
    mh.insert(593)
    mh.insert(9123)
    mh.insert(293)

    mh.print_heap()

    mh.remove()

    assert mh.heap[0] == min(mh.heap)

    mh.print_heap()
