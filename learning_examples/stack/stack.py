class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node<value: {self.value}>"


class Stack:
    def __init__(self, value: int = None):
        if value is not None:
            new_node = Node(value=value)

            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def push(self, value: int):
        """Push a value to the top of the stack"""
        new_node = Node(value=value)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop(self) -> Node | None:
        """Pop the top item of the stack"""
        if self.top is None:
            return None

        temp = self.top
        self.top = temp.next
        temp.next = None

        self.height -= 1
        return temp

    def print_stack(self) -> None:
        """Prints the stack information, created for debugging purposes"""
        node = self.top

        if self.height == 0:
            return None

        item_index = 0
        print("=-=" * 10)
        while node is not None:
            print(f"Index {item_index}: {node.value}")
            node = node.next
            item_index += 1

        print("=-="*10)
        print("Top: ", self.top.value)
        print("Height: ", self.height)
        print("=-=" * 10)


if __name__ == "__main__":
    stack = Stack(23)
    stack.push(25)
    print(stack.pop())
    stack.push(33)
    stack.print_stack()
