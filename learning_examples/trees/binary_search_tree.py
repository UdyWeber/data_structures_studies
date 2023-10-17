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

    def breadth_first_search(self):
        queue = [self.root]
        results = []

        while queue:
            node = queue.pop(0)
            results.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return results

    def depth_first_search_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)

            if current_node.left:
                traverse(current_node.left)

            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def depth_first_search_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)

            if current_node.right:
                traverse(current_node.right)

            results.append(current_node.value)

        traverse(self.root)
        return results

    def depth_first_search_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)

            results.append(current_node.value)

            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid_bst(self):
        nodes_values = self.depth_first_search_in_order()
        for i in range(1, len(nodes_values)):
            if nodes_values[i] <= nodes_values[i - 1]:
                return False
        return True

    def kth_smallest(self, index: int):

        stack = []
        node = self.root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            index -= 1
            if index == 0:
                return node.value

            node = node.right


if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst.kth_smallest(1))  # Expected output: 2
    print(bst.kth_smallest(3))  # Expected output: 4
    print(bst.kth_smallest(6))  # Expected output: 7
