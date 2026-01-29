"""
Given a sorted array arr[]. Convert it into a Height Balanced Binary Search Tree (BST) and return the root of the BST.

Height-balanced BST means a binary tree in which the depth of the left subtree and the right subtree of every node never differ by more than 1.

Note: You can return any BST, the driver code will check the BST, and print true if it is a Height-balanced BST else print false.

Examples :

Input: arr[] = [10, 20, 30]
Output: true
Explanation: Only possible Height Balanced BST will be [20, 10, 30]


Input: arr[] = [1, 5, 9, 14, 23, 27]
Ouput: true
Explanation: One of the possible Height Balanced BST will be [9, 1, 23, N, 5, 14, 27]

Constraints:
1 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node

from collections import deque


class Solution:
    def sorted_array_to_bst(self, arr):
        return self.construct_bst_from_inorder(arr, 0, len(arr) - 1)

    def construct_bst_from_inorder(self, inorder_traversal, low, high):
        if low > high:
            return None

        mid = low + (high - low) // 2
        root = Node(inorder_traversal[mid])

        root.left = self.construct_bst_from_inorder(inorder_traversal, low, mid - 1)
        root.right = self.construct_bst_from_inorder(inorder_traversal, mid + 1, high)
        return root

    def sorted_array_to_bst_ittr(self, arr):
        if arr is None or not len(arr):
            return None

        input_arr = [None if val == "N" else int(val) for val in arr]

        que = deque()
        low = 0
        high = len(input_arr) - 1
        mid = low + (high - low) // 2
        root = Node(input_arr[mid])
        que.append((root, low, high))

        while que:
            curr, low, high = que.popleft()
            mid = low + (high - low) // 2

            if low < mid:
                idx = low + ((mid - 1) - low) // 2
                curr.left = Node(input_arr[idx])
                que.append((curr.left, low, mid - 1))

            if high > mid:
                idx = (mid + 1) + (high - (mid + 1)) // 2
                curr.right = Node(input_arr[idx])
                que.append((curr.right, mid + 1, high))

        return root


def main():
    arr = input("Enter the tree level order: ").strip().split()
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()

    soln = Solution()
    result = soln.sorted_array_to_bst_ittr(arr)
    bst.print_tree(result)


if __name__ == "__main__":
    main()
