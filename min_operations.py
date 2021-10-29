import Queue


class Node:
    def __init__(self, value, ops):
        self.value = value
        self.ops = ops


def min_operations(x, y):
    queue = Queue.Queue()
    queue.put(Node(x, 0))

    visited = set()

    while queue:
        curr = queue.get()

        if curr.val == y:
            return curr.ops

        if curr.val * 2 == y or curr - 1 == y:
            return curr.ops + 1

        if curr.val * 2 not in visited:
            queue.put(Node(curr.val * 2, curr.ops + 1))
        if curr.val - 1 not in visited and curr.val - 1 >= 0:
            queue.put(Node(curr.val - 1, curr.ops + 1))


print(min_operations(2, 5))
