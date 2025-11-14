from typing import List
from queue import Queue


# Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    """
    The array representation usually stores "binary heaps" or "complete binary trees."
    And in platform like GeeksForGeeks/Leetcode compact array form are used as input
    to have less None values
    """

    def build_tree(self, lst: List) -> BinaryTreeNode | None:
        if not lst:
            self.root = None
            return None

        size = len(lst)
        queue = Queue()

        # Root of the tree using first element of parameter list
        root = BinaryTreeNode(lst[0])
        queue.put(root)

        # Iterating over the input list and using a queue to procee
        i = 1
        while i < size:
            curr = queue.get()
            if i < size:
                if lst[i] is not None:
                    curr.left = BinaryTreeNode(lst[i])
                    queue.put(curr.left)
                i += 1
            if i < size:
                if lst[i] is not None:
                    curr.right = BinaryTreeNode(lst[i])
                    queue.put(curr.right)
                i += 1

        self.root = root
        return self.root

    """
    To use classical tree building approach, the list argument should be in long form
    Having all the None nodes if it exists for all levels, as "binary heap" or "complete binary tree".
    """

    def build_tree_classic_iterative(self, lst):
        if not lst:
            self.root = None
            return None

        size = len(lst)
        # Creating list of all the node from parameter list data
        nodes = [None if val is None else BinaryTreeNode(val) for val in lst]
        root = nodes[0]

        # Linking the left and right child using binary tree property
        for i in range(size):
            curr_node = nodes[i]
            if curr_node is None:
                continue

            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2

            if left_child_index < size and nodes[left_child_index] is not None:
                curr_node.left = nodes[left_child_index]
            if right_child_index < size and nodes[right_child_index] is not None:
                curr_node.right = nodes[right_child_index]

        self.root = root
        return self.root

    def build_tree_classic_recu(self, lst: List, size: int, i=0):
        root = None
        if i < size and lst[i] is not None:
            root = BinaryTreeNode(lst[i])
            root.left = self.build_tree_classic_recu(lst, size, 2 * i + 1)
            root.right = self.build_tree_classic_recu(lst, size, 2 * i + 2)

        self.root = root
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
