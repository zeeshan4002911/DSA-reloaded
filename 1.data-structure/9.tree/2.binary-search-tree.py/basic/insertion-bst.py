"""
Given the root of a binary search tree and a value key. Insert a new node with a value equal to key into the tree and return the root of the modified tree after inserting the value.

Note: All the nodes have distinct values in the BST and the new value to be inserted is not present in the BST.

Examples :

Input: root = [2, 1, 3], key = 4

Output: [2, 1, 3, N, N, N, 4]
Explanation: After inserting the node 4, the new tree will be [2, 1, 3, N, N, N, 4].

Input: root = [2, 1, 3, N, N, N, 6], key = 4

Output: [2, 1, 3, N, N, N, 4, N, 6]
Explanation: After inserting the node 4, the new tree will be [2, 1, 3, N, N, N, 4, N, 6].

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^9
1 ≤ key ≤ 10^9

Expected Complexities
Time Complexity: O(h)
Auxiliary Space: O(1)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node


class Solution:
    def insertion(self, root, key):
        if root is None:
            new_node = Node(key)
            return new_node

        curr = root
        while curr:
            # Condition to traverse right subtree or insert in case key is more than current node
            if curr.data < key:
                if curr.right is None:
                    curr.right = Node(key)
                    break
                else:
                    curr = curr.right
            # Condition to traverse left subtree or insert in case key is less than current node
            elif curr.data > key:
                if curr.left is None:
                    curr.left = Node(key)
                    break
                else:
                    curr = curr.left
            # In case of duplicate key
            else:
                break

        return root


def main():
    arr = input("Enter the tree level order: ").strip().split()
    key = int(input("Enter the key to insert: ").strip())
    arr = [int(val) if isinstance(val, int) else val for val in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)

    soln = Solution()
    soln.insertion(root, key)
    bst.print_tree()


if __name__ == "__main__":
    main()
