class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node | None = None

    def __repr__(self):
        return f"Node<value: {self.value}>"


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
        elif index == self.length:
            return self.append(value)
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
        elif index == self.length - 1:
            return self.pop()
        else:
            node_before = self.get(index=index - 1)
            node_to_removed = node_before.next

            node_before.next = node_to_removed.next
            node_to_removed.next = None

            self.length -= 1
            return node_to_removed

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

    def reverse(self):
        """Reverses the values in the LinkedList"""
        # This method is a bit tricky, so we are going to explain step by step
        # First we need to reverse our head and tail and store the old head value
        current_node = self.head
        self.head = self.tail
        self.tail = current_node

        # Now we need to create our pivots to help knowing where we are on the linked list
        before = None

        # Now the iteration starts
        while current_node is not None:
            # Here we define the node that comes after the one we are iterating over
            after = current_node.next

            # Here we store the value of before flipping the pointer
            # to the before value of the current in the item instead of the next
            current_node.next = before

            # Here we walk ahead on the list to continue iterating
            before = current_node
            current_node = after

        return True

    def print_list(self) -> None:
        """Prints the list information, created for debugging purposes"""
        node = self.head
        values = []

        if self.length == 0:
            return None

        item_index = 0
        print("=-=" * 10)
        while node is not None:
            values.append(node.value)
            print(f"Index {item_index}: {node.value}")
            node = node.next
            item_index += 1

        print("=-="*10)
        print("Head: ", self.head.value)
        print("Tail: ", self.tail.value)
        print("Length: ", self.length)
        print("=-=" * 10)

        return values

    def find_middle_by_length(self):
        index = self.length // 2

        node = self.get(index=index)
        return node

    def find_middle_node(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def bubble_sort(self):
        if self.length < 2:
            return None

        sorted_until = None

        # If it reaches the 2nd node on the list it means it's already sorted
        # Cause head and tail are already swapped with their respective values
        while sorted_until != self.head.next:
            current = self.head

            # Always cutting the iterations by 1
            # Assuming that the last node iterated is sorted
            while current.next != sorted_until:
                n1 = current.next

                if current.value > n1.value:
                    current.value, n1.value = n1.value, current.value

                current = current.next

            # Setting the record of the last node of the previous iteration
            sorted_until = current

    def selection_sort(self):
        ...


if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.bubble_sort()
    my_linked_list.print_list()
