"""
Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.
 Example 1:

Input:
      1
    /   \
   2     3
Output: 
1 2 3
Explanation:
The converted BST will be 
      2
    /   \
   1     3


Example 2:

Input:
          1
       /    \
     2       3
   /        
 4       
Output: 
1 2 3 4
Explanation:
The converted BST will be

        3
      /   \
    2     4
  /
 1

Your Task:
You don't need to read input or print anything. Your task is to complete the function binaryTreeToBST() which takes the root of the Binary tree as input and returns the root of the BST. The driver code will print inorder traversal of the converted BST.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 10^5
"""

import os, sys

# Importing binary tree helper to build tree instead of bst builder
sys.path.append(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "..", "..", "1.binary-tree"
    )
)
from binary_tree_helper import BinaryTree

from collections import deque


class Solution:
    def binary_tree_to_bst(self, root):
        if root is None:
            return root

        # DFS pre-order traversal of binary tree using stack to collect all the nodes
        nodes = []
        st = deque([root])
        while st:
            curr = st.pop()
            nodes.append(curr.data)

            if curr.right:
                st.append(curr.right)
            # Adding left last so that it gets popped first and do root -> left -> right
            if curr.left:
                st.append(curr.left)

        # Sorting in non-decreasing order to use as bst inorder result
        nodes.sort()

        # Doing in-order traversal using stack of tree and updating to sorted values
        st.clear()
        curr = root
        i = 0
        while curr or st:
            # Going to left most node first
            while curr:
                st.append(curr)
                curr = curr.left

            curr = st.pop()
            # Updating the current node value from sorted node to do update of exisitng tree
            curr.data = nodes[i]
            i += 1

            # Either null or right node, null will pull from stack and backtrack to parent
            curr = curr.right

        return root


def main():
    arr = input("Enter the tree level order: ").strip().split()
    arr = [x.replace(",", "").strip() for x in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    bt.print_tree()

    soln = Solution()
    result = soln.binary_tree_to_bst(root)
    bt.print_tree(result)


if __name__ == "__main__":
    main()
