from queue import Queue
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Building bst using the min and max range to validate the bst rule
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


    # Building bst using sorted array input, using index as range for positioning in proper place
    def build_bst_from_sorted(self, arr):
        if arr is None or not len(arr):
            return None

        input_arr = [None if val == "N" else int(val) for val in arr]

        # Deque is better than queue module in single threaded use
        que = deque()
        low = 0
        high = len(input_arr) - 1

        # mid point of inorder result or sorted input for balanced binary search tree
        mid = low + (high - low) // 2
        root = Node(input_arr[mid])
        # Index as range for calculation for each node
        que.append((root, low, high))

        while que:
            curr, low, high = que.popleft()
            mid = low + (high - low) // 2

            # If left subtree exists i.e., values are there in left side of current node
            if low < mid:
                idx = low + ((mid - 1) - low) // 2
                curr.left = Node(input_arr[idx])
                que.append((curr.left, low, mid - 1))

            # If right subtree exists i.e., values are there in right side of current node
            if high > mid:
                idx = (mid + 1) + (high - (mid + 1)) // 2
                curr.right = Node(input_arr[idx])
                que.append((curr.right, mid + 1, high))

        return root

    # Recursive bst build using sorted array input, using index as range for positioning in proper place
    def build_bst_from_sorted_rec(self, arr, low, high):
        if low > high:
            return None

        mid = low + (high - low) // 2
        root = Node(arr[mid])

        root.left = self.build_bst_from_sorted_rec(arr, low, mid - 1)
        root.right = self.build_bst_from_sorted_rec(arr, mid + 1, high)
        return root

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
