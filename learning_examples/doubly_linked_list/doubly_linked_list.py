class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node<value: {self.value}>"


class DoublyLinkedList:
    def __init__(self, value: int = None):
        if value is not None:
            new_node = Node(value=value)

            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail = None
            self.head = None
            self.length = 0

    def append(self, value: int):
        new_node = Node(value=value)

        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        old_tail = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.prev
            self.tail.next = None
            old_tail.prev = None

        self.length -= 1

        return old_tail

    def prepend(self, value: int):
        new_node = Node(value=value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None

        last_head = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = last_head.next
            self.head.prev = None
            last_head.next = None

        self.length -= 1
        return last_head

    def get(self, index: int) -> Node | None:
        if self.length == 0 or index >= self.length:
            return None

        if index < 0:
            absolute_index = index * -1

            if absolute_index > self.length:
                return None

            current_node = self.tail
            for _ in range(absolute_index - 1):
                current_node = current_node.prev
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next

        return current_node

    def set_value(self, index: int, value: int):
        node = self.get(index=index)

        if node is None:
            return False

        node.value = value
        return True

    def insert(self, index: int, value: int):
        if index == 0:
            return self.prepend(value=value)
        elif index >= self.length:
            return self.append(value=value)
        else:
            replaced_node = self.get(index)

            if replaced_node is None:
                return False

            new_node = Node(value=value)

            replaced_node.prev.next = new_node
            new_node.prev = replaced_node.prev
            new_node.next = replaced_node
            replaced_node.prev = new_node

        self.length += 1
        return True

    def swap_first_last(self):
        if self.head == self.tail or self.head is None:
            return

        self.head.value, self.tail.value = self.tail.value, self.head.value

    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            node_to_remove = self.get(index)

            before = node_to_remove.prev
            before.next = node_to_remove.next
            node_to_remove.next.prev = before

            self.length -= 1
            return node_to_remove

    def reverse(self):
        # We have to set our current to the head of the list
        current = self.head

        while current is not None:
            # As you're willing to walk back on the list, you might notice that you have to invert your path
            # So every time we have to swap the prev and next values in order to achieve the right path to follow
            current.next, current.prev = current.prev, current.next

            # Always moving back on the list
            current = current.prev

        # Have you swapped the pointers path, now head.next is None, so in order to move forward in the list
        # You have to set head as tail cause tail.next is not None and it points to the inverted Path list
        self.tail, self.head = self.head, self.tail

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

        print("=-=" * 10)
        print("Head: ", self.head.value)
        print("Tail: ", self.tail.value)
        print("Length: ", self.length)
        print("=-=" * 10)


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)
    doubly_linked_list.append(4)
    doubly_linked_list.reverse()
    doubly_linked_list.print_list()
