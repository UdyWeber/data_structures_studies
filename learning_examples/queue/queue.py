class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node<value: {self.value}>"


class Queue:
    def __init__(self, value: int = None):
        if value is None:
            self.first = None
            self.last = None
            self.length = 0
        else:
            new_node = Node(value)

            self.first = new_node
            self.last = new_node
            self.length = 1

    def enqueue(self, value: int):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self) -> Node | None:
        if self.length == 0:
            return None

        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None

        self.length -= 1
        return temp

    def list_queue(self):
        # We are looking the queue like this => process | 1 2 3 4
        # That's why we start from the first
        current = self.first

        while current is not None:
            print(current)
            current = current.next

        print(f"Queue length: {self.length}")


class StackQueue:
    def __init__(self):
        # Principal queue
        self.stack1 = []
        # Helper to perform enqueue dequeue
        self.stack2 = []

    def enqueue(self, value: int):
        # We have to make it became the last to go out when enqueued
        while not self.is_empty():
            # Reverting the queue
            self.stack2.append(self.stack1.pop())

        # Adding new value to the helper stack
        self.stack1.append(value)

        # Dumping reversing again the values to achieve the new order on the queue
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None

        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

    def print_list(self):
        for item in reversed(self.stack1):
            print(item)


if __name__ == "__main__":
    queue = StackQueue()
    queue.enqueue(6)
    queue.enqueue(8)
    queue.enqueue(420)
    queue.enqueue(69)
    queue.print_list()
    print(f"Tirado da lista: {queue.dequeue()}")
