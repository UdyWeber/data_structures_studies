class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node<value: {self.value}, next: {self.next}>"


class LinkedList:
    def __init__(self, value=None):
        # create a new Node

        if value is not None:
            new_node = Node(value=value)

            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def append(self, value):
        # Create a new node and add to the end
        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        # Create a new node and add to the beginning
        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, index: int, value,):
        # Create a new node iterate the list to the index and add new node to it
        new_node = Node(value=value)
        node = self.head

        for _ in range(index):
            node = node.next

        new_node.next = node.next
        node.next = new_node

        self.length += 1

    def print_list(self):
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next


my_linked_list = LinkedList(3)
my_linked_list.append(95)
my_linked_list.prepend(194)
my_linked_list.insert(value=123, index=1)

print("Tail: ", my_linked_list.tail.value)
print("Head: ", my_linked_list.head.value)
print("Length: ", my_linked_list.length)

my_linked_list.print_list()
