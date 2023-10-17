class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f"Node<value: {self.value}>"


class RecursiveBinarySearchTree:
    def __init__(self, value: int = None):
        if value is None:
            self.root = None
        else:
            new_node = Node(value)
            self.root = new_node

    def __r_contains(self, current_node: Node, value):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node: Node, value):
        if current_node is None:
            return Node(value)
        elif current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node

    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None or (current_node.left is None and current_node.right is None):
            return None
        elif value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)


if __name__ == "__main__":
    rbst = RecursiveBinarySearchTree()
    rbst.r_insert(12)
    rbst.r_insert(20)
    rbst.r_insert(9)
    rbst.r_insert(29)
    rbst.r_insert(28)
    rbst.delete_node(20)

    print(rbst)
