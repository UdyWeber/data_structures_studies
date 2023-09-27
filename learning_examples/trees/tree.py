class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f"Node<value: {self.value}>"


class BinarySearchTree:
    def __init__(self, value: int = None):
        if value is None:
            self.root = None
        else:
            new_node = Node(value)
            self.root = new_node

    def insert(self, value) -> bool:
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root

            while current_node is not None:
                if value == current_node.value:
                    return False

                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break

                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break

                    current_node = current_node.right

        return True

    def contains(self, value) -> bool:
        temp = self.root

        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True

        return False


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(69)
    tree.insert(420)
    tree.insert(9)
    tree.insert(18)
    tree.insert(596)
    tree.insert(18)
    tree.insert(130)

    print(tree.contains(18))
    print(tree)
