from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def build_bst(self, arr):
        if arr is None:
            self.root = None
            return None

        size = len(arr)
        if size < 1:
            self.root = None
            return None

        lst = [None if val == "N" else int(val) for val in arr]
        i = 0
        node = Node(lst[i])
        self.root = node

        q = Queue()
        q.put((node, -float("inf"), +float("inf")))
        i += 1

        while not q.empty() and i < size:
            curr, min_val, max_val = q.get()

            if i < size:
                if lst[i] is not None and min_val < lst[i] < curr.data:
                    node = Node(lst[i])
                    curr.left = node
                    q.put((curr.left, min_val, curr.data))

                i += 1

            if i < size:
                if lst[i] is not None and curr.data < lst[i] < max_val:
                    node = Node(lst[i])
                    curr.right = node
                    q.put((curr.right, curr.data, max_val))

                i += 1

        return self.root

    ### For Printing level wise tree for visualization
    def print_tree(self, root=None):
        root = root or self.root

        # Helper function to print the tree in a structured way
        levels = []
        self._collect_levels(root, 0, levels)

        for i, level in enumerate(levels):
            print(f"Level {i}: ", end="")
            print(" -> ".join(str(node.data) for node in level if node is not None))

    def _collect_levels(self, node, level, levels):
        if node is None:
            return

        if len(levels) <= level:
            levels.append([])

        levels[level].append(node)

        self._collect_levels(node.left, level + 1, levels)
        self._collect_levels(node.right, level + 1, levels)
