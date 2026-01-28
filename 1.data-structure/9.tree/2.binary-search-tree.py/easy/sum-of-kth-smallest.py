"""
Given a Binary Search Tree. Find sum of all elements smaller than and equal to Kth smallest element.

Example 1:

Input: 
          20
        /    \
       8     22
     /    \
    4     12
         /    \
        10    14   , K=3

Output: 22
Explanation:
Sum of 3 smallest elements are: 
4 + 8 + 10 = 22

Example 2:

Input:
     10
    /  \
   5    11
  / \ 
 4   7
      \
       8 , K=2

Output: 9
Explanation:
The sum of two smallest elements 
is 4+5=9.

 
Your task:
You don't need to read input or print anything. Your task is to complete the function sum() which takes the root node and an integer K as input parameters and returns the sum of all elements smaller than and equal to kth smallest element.
 
Expected Time Complexity: O(K)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=Number of nodes in BST<=100
1<=K<=N
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree

from queue import LifoQueue


class Solution:
    def sum_of_kth_smallest_element_ittr(self, root, k):
        k_sum = 0
        if root is None:
            return k_sum

        k_count = 0
        st = LifoQueue()
        curr = root

        while curr or not st.empty():
            # Inorder traversal, traversing to the left most node
            while curr:
                st.put(curr)
                curr = curr.left

            curr = st.get()

            # Counting from the smallest element
            k_count += 1
            if k_count <= k:
                k_sum += curr.data
            else:
                # Stopping the traversal after sum calc complete
                break

            curr = curr.right

        return k_sum

    def sum_of_kth_smallest_element_rec(self, root, k):
        if root is None:
            return 0

        self.k_sum = 0
        self.k_count = 0
        self.sum_of_kth_smallest_element_rec_helper(root, k)
        return self.k_sum

    def sum_of_kth_smallest_element_rec_helper(self, root, k):
        if not root or self.k_count > k:
            return

        self.sum_of_kth_smallest_element_rec_helper(root.left, k)

        self.k_count += 1
        if self.k_count <= k:
            self.k_sum += root.data
        else:
            return

        if self.k_count <= k:
            self.sum_of_kth_smallest_element_rec_helper(root.right, k)


def main():
    arr = input("Enter the tree level order: ").strip().split()
    k = int(input("Enter the value of k: ").strip())
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.sum_of_kth_smallest_element_rec(root, k)
    print(result)


if __name__ == "__main__":
    main()
