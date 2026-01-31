"""
Given a BST, modify it so that all greater values in the given BST are added to every node.

Example 1:

Input:
           50
         /    \
        30    70
      /  \    / \
     20  40  60 80
Output: 350 330 300 260 210 150 80
Explanation:The tree should be modified to
following:
             260
          /      \
        330       150
       /   \     /    \
    350   300   210    80

Example 2:

Input:
          2
        /   \
       1     5
            /  \
           4    7
Output: 19 18 16 12 7

Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes one argument: the root of the BST. The function should contain the logic to modify the BST so that in the modified BST, every node has a value equal to the sum of its value in the original BST and values of all the elements larger than it in the original BST. Return the root of the modified BST. The driver code will print the inorder traversal of the returned BST/

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1<=N<=100000

Note: The Input/Output format and Example is given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree

from collections import deque


class Solution:
    def add_all_greater_values_to_every_node_in_bst(self, root):
        curr = root
        st = deque()
        # Sum to track all the greater values before current node
        greater_sum = 0

        # Reverse in-order traversal, as the right most node has maximum value in bst
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.right

            curr = st.pop()
            
            # Cache reference to add to running sum
            curr_data_ref = curr.data
            # Updating the node directly in-place
            curr.data += greater_sum
            # Increasing the sum by adding previous greater values
            greater_sum += curr_data_ref

            curr = curr.left

        return root


def main():
    arr = input("Enter the tree level order: ").strip().split()
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.add_all_greater_values_to_every_node_in_bst(root)
    bst.print_tree(result)

if __name__ == "__main__":
    main()