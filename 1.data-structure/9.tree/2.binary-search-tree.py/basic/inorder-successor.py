"""
Given a BST, and a reference to a Node k in the BST. Find the Inorder Successor of the given node in the BST. If there is no successor, return -1. 

Examples :

Input: root = [2, 1, 3], k = 2
      2
    /   \
   1     3
Output: 3 
Explanation: Inorder traversal : 1 2 3 Hence, inorder successor of 2 is 3.

Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 8
             20
            /   \
           8     22
          / \
         4   12
            /  \
           10   14
Output: 10
Explanation: Inorder traversal: 4 8 10 12 14 20 22. Hence, successor of 8 is 10.

Input: root = [2, 1, 3], k = 3
      2
    /   \
   1     3
Output: -1 
Explanation: Inorder traversal : 1 2 3 Hence, inorder successor of 3 is null.

Constraints:
1 <= n <= 10^5, where n is the number of nodes

Expected Complexities
Time Complexity: O(Height of the BST)
Auxiliary Space: O(1)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node


class Solution:
    def get_inorder_successor_ittr(self, root, x):
        if root is None:
            return -1

        succ_node = None
        curr = root
        while curr:
            if curr.data > x.data:
                # Step 2: Post finding the value it go to left side always
                # as x will be greater in it's subtree after step 1
                succ_node = curr
                curr = curr.left
            elif curr.data < x.data:
                curr = curr.right
            else:
                # Step 1: Case where node value is found
                curr = curr.right

        return -1 if succ_node is None else succ_node.data


def main():
    arr = input("Enter the tree level order: ").strip().split()
    x = int(input("Enter the value of x: ").strip())
    x_node = Node(x)
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.get_inorder_successor_ittr(root, x_node)
    print(result)


if __name__ == "__main__":
    main()


"""
We begin traversal from root. For every node, we need to take care of 3 cases for to find its inorder successor.

    1) Right child of node is not NULL : The successor will be the leftmost node in its right subtree.
    2) The node is the Rightmost in Tree : The successor is NULL. For example, node 6 in the above diagram.
    3) If right child of the node is NULL : The successor must be an ancestor. 
    Travel up using the parent pointer until we see a node which is left child of its parent. 
    The parent of such a node is the successor.
"""
