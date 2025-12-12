"""
Given the root of a Binary Tree, your task is to return its Level Order Traversal.

Note: A level order traversal is a breadth-first search (BFS) of the tree. It visits nodes level by level, starting from the root, and processes all nodes from left to right within each level before moving to the next.

Examples:

Input: root = [1, 2, 3]
   1
 /   \
2     3

Output: [[1], [2, 3]]
Explanation: We start with the root node 1, so the first level of the traversal is [1]. Then we move to its children 2 and 3, which form the next level, giving the final output [[1], [2, 3]].

Input: root = [10, 20, 30, 40, 50]
    10
   /  \
  20  30
 /  \
40  50
Output: [[10], [20, 30], [40, 50]]
Explanation: We begin with the root node 10, which forms the first level as [10]. Its children 20 and 30 make up the second level, and their children 40 and 50 form the third level, resulting in [[10], [20, 30], [40, 50]].

Constraints:
1 ≤ number of nodes ≤ 3*10^4
0 ≤ node->data ≤ 10^9

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

import sys, os
from queue import Queue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Traversal:
    def level_order_traversal_rec(self, root):
        return self._helper(root, 0, [])

    def _helper(self, node, curr_level, levels):
        if node is None:
            return levels

        if len(levels) <= curr_level:
            levels.append([])

        levels[curr_level].append(node.data)

        self._helper(node.left, curr_level + 1, levels)
        self._helper(node.right, curr_level + 1, levels)

        return levels

    def level_order_traversal_ittr(self, root):
        if root is None:
            return []

        result = []
        queue = Queue()
        queue.put((root, 0))

        # BFS - Breadth First Search using queue for backtracking
        while not queue.empty():
            curr, level_num = queue.get()

            # logic to add new list based on level
            if len(result) <= level_num:
                result.append([])
            result[level_num].append(curr.data)

            if curr.left:
                queue.put((curr.left, level_num + 1))

            if curr.right:
                queue.put((curr.right, level_num + 1))

        return result


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    # bt.print_tree()

    traversal = Traversal()
    # result = traversal.level_order_traversal_rec(root)
    result = traversal.level_order_traversal_ittr(root)
    print(result)


if __name__ == "__main__":
    main()
