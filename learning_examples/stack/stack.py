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


class ListStack:
    def __init__(self, value: int | str = None):
        if value is None:
            self.stack_list = []
        else:
            self.stack_list = [value]

    def push(self, value: int | str):
        self.stack_list.append(value)

    def pop(self) -> int | str | None:
        if not self.stack_list:
            return None

        return self.stack_list.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def is_empty(self):
        return self.size() == 0

    def print_stack(self):
        for node in self.stack_list:
            print(node)

        print(f"Height: {len(self.stack_list)}")


def is_balanced_parentheses(string_with_parentheses: str) -> bool:
    my_stack = ListStack()

    for char in string_with_parentheses:
        if char == "(":
            my_stack.push(char)
        elif char == ")":
            if my_stack.is_empty() or my_stack.pop() != "(":
                return False

    return my_stack.is_empty()


def reverse_string(string_to_reverse: str) -> str:
    my_stack = ListStack()

    for char in string_to_reverse:
        my_stack.push(char)

    reversed_string = ""

    while not my_stack.is_empty():
        reversed_string += my_stack.pop()

    return reversed_string


def sort_stack(input_stack: ListStack):
    sorted_stack = ListStack()

    while not input_stack.is_empty():
        temp = input_stack.pop()

        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            input_stack.push(sorted_stack.pop())

        sorted_stack.push(temp)

    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())


if __name__ == "__main__":
    my_stack = ListStack()
    my_stack.push(3)
    my_stack.push(1)
    my_stack.push(5)
    my_stack.push(4)
    my_stack.push(2)

    my_stack.print_stack()
    sort_stack(my_stack)
    my_stack.print_stack()
