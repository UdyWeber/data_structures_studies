class MaxHeap:
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

    def insert(self, value):
        self.heap.append(value)
        index_of_value = len(self.heap) - 1

        while index_of_value > 0 and self.heap[index_of_value] > self.heap[self._parent(index_of_value)]:
            parent_index = self._parent(index_of_value)

            self._swap(index_of_value, parent_index)
            index_of_value = parent_index

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

                print(f"[LEVEL {first_parent + 1}] " + " -> ".join(path[::-1]))


if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(23)
    mh.insert(123)
    mh.insert(12)
    mh.insert(1000)
    mh.insert(75)
    mh.insert(1500)
    mh.insert(593)
    mh.insert(9123)

    mh.print_heap()
