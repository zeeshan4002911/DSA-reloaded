"""
Given the root of a Binary Search Tree. Your task is to find the minimum element in this given BST.

Examples

Input: root = [5, 4, 6, 3, N, N, 7, 1]
ex-1
Output: 1
Explanation: The minimum element in the given BST is 1.

Input: root = [10, 5, 20, 2]
ex-2
Output: 2
Explanation: The minimum element in the given BST is 2.

Constraints:
0 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree


class Solution:
    def minimum_value_ittr(self, root):
        if root is None:
            return -1

        curr = root
        while curr and curr.left:
            # Traversing left node as the left most node should have minimum value
            # BST Rule: In-order of bst gives sorted values
            curr = curr.left

        return curr.data
    
    def minimum_value_rec(self, root, min_value = -1):
        if root is None:
            # Returning the parent node value, in case of minimum it's left most leaf 
            # and default -1 for single root node
            return min_value
        
        return self.minimum_value_rec(root.left, root.data)



def main():
    arr = input("Enter the tree level order: ").strip().split()
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.minimum_value_ittr(root)
    print(result)


if __name__ == "__main__":
    main()
