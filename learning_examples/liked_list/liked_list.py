class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node<value: {self.value}, next: {self.next}>"


class LinkedList:
    def __init__(self, value: int = None):
        if value is not None:
            new_node = Node(value=value)

            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def append(self, value: int) -> bool:
        """Add a value at the end of the list"""
        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value: int) -> bool:
        """Add a value to the front of the list"""
        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop(self) -> Node | None:
        """Remove and returns the last node in the list"""
        node_to_pop = self.tail

        if self.length == 1:
            self.make_empty()
        elif self.length > 1:
            penultimate = self.head

            while penultimate.next.next is not None:
                penultimate = penultimate.next

            self.tail = penultimate
            self.tail.next = None
            self.length -= 1

        return node_to_pop

    def pop_first(self) -> Node | None:
        """Remove and returns the first node in the list"""
        node_to_pop = self.head

        if self.length == 1:
            self.make_empty()
        elif self.length > 1:
            new_head = self.head.next

            self.head.next = None
            self.head = new_head
            self.length -= 1

        return node_to_pop

    def make_empty(self) -> None:
        """Empty's the list"""
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, index: int, value: int) -> bool:
        """Create a new node iterate the list to the index and add new node to it"""
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value=value)
        else:
            node_before = self.get(index=index - 1)

            if not node_before:
                return False

            new_node = Node(value=value)

            new_node.next = node_before.next
            node_before.next = new_node

            self.length += 1
            return True

    def remove(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        else:
            node_before = self.get(index=index - 1)
            node_to_removed = node_before.next

            node_before.next = node_to_removed.next
            node_to_removed.next = None

            self.length -= 1
            return node_to_removed

    def print_list(self) -> None:
        """Prints the list information, created for debugging purposes"""
        node = self.head

        if self.length == 0:
            return None

        item_index = 0
        print("=-=" * 10)
        while node is not None:
            print(f"Index {item_index}: {node.value}")
            node = node.next
            item_index += 1

        print("=-="*10)
        print("Head: ", my_linked_list.head.value)
        print("Tail: ", my_linked_list.tail.value)
        print("Length: ", my_linked_list.length)
        print("=-=" * 10)

    def get(self, index: int) -> Node | None:
        if self.length == 0 or index < 0 or index >= self.length:
            return None

        node_to_get = self.head
        for _ in range(index):
            node_to_get = node_to_get.next

        return node_to_get

    def set_value(self, index: int, value: int) -> bool:
        node_to_set = self.get(index=index)

        if not node_to_set:
            return False

        node_to_set.value = value
        return True


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.print_list()
    my_linked_list.insert(index=2, value=19)
    my_linked_list.print_list()
    # my_linked_list.print_list()
