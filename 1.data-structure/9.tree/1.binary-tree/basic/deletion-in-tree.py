"""
Given a binary tree with nodes where all elements are unique, implement a function that deletes a node with a specified value (key) from the tree.
When a node is deleted, the tree should shrink from the bottom, meaning the deleted node is replaced by the bottom-most, right-most node in the tree.
After deletion, the binary tree will be printed using in-order traversal.

Examples:

Input: root[] = [10, 20, 30], key = 10
    10
   /  \
  20   30
Output: [20, 30]
Explanation:
The node with the key 10 (the root) is to be deleted. The bottom-most, right-most node (30) replaces node 10. The modified tree becomes: 
    30
   /
  20
The inorder traversal of the modified tree is [20, 30].

Input: root[] = [10, 20, 30, N, N, N, 40], key = 20
    10
   /  \
  20   30
        \
         40
Output: [40, 10, 30]
Explanation: 
The node with the key 20 is to be deleted. The bottom-most, right-most node (40) replaces node 20. The modified tree becomes:
    10
   /  \
  40   30
The inorder traversal of the modified tree is [40, 10, 30].

Constraints:
1 ≤ number of nodes ≤ 10^4
1 ≤ node->data ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

import sys, os
from queue import Queue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree, BinaryTreeNode


class Solution:
    def deletion_in_tree_ittr(self, root, key):
        if root is None:
            return []

        queue = Queue()
        queue.put((root, None, None))
        delete_parent, delete_child, delete_child_pos = None, None, None
        last_parent, last_child, last_child_pos = None, None, None

        while not queue.empty():
            (curr, parent, direction) = queue.get()
            last_child, last_parent, last_child_pos = curr, parent, direction
            if not delete_parent and curr.data == key:
                delete_child, delete_parent, delete_child_pos = curr, parent, direction

            if curr.left:
                queue.put((curr.left, curr, "l"))
            if curr.right:
                queue.put((curr.right, curr, "r"))

        # Not found case
        if delete_child is None or last_child is None:
            return root
        
        # Swpping of node data from delete position to last
        delete_child.data, last_child.data = last_child.data, delete_child.data

        # Removing the link of last node
        if last_child_pos == "r":
            last_parent.right = None
        elif last_child_pos == "l":
            last_parent.left = None

        return root


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    key = input("Enter key: ").strip()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    result = soln.deletion_in_tree_ittr(root, key)
    # print(result)
    bt.print_tree(root)


if __name__ == "__main__":
    main()
