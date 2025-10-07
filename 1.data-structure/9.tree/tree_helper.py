# Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, lst):
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
        return root

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
