class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data <= node.data:
            if node.left:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def isBalanced(self, node):
        if not node:
            return True

        lh = self.get_height(node.left)
        rh = self.get_height(node.right)

        if abs(lh - rh) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right):
            return True
        return False

    def get_height(self, node):
        if not node:
            return 0
        else:
            i = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return i


def main():
    bst = BST()
    nodes = [8, 3, 10, 1, 6, 4, 7, 13, 14]
    for n in nodes:
        bst.add(n)

    print(bst.isBalanced(bst.root))


if __name__ == '__main__':
    main()
