"""
Given an array arr of size N, determine whether this array represents an inorder traversal of a BST.

Note: All keys in BST must be unique.

Example 1:

Input:
N = 3
arr = {2, 4, 5}
Output: 1
Explaination:
Given array is inorder traversal for the following tree:


Example 2:

Input:
N = 3
arr = {2, 4, 1}
Output: 0
Explaination:
Given array can not represent any BST.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isRepresentingBST() which takes the array arr[] and its size N as input parameters and returns 1 if array represents Inorder traversal of a BST, else returns 0.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10^5
1 ≤ arr[i] ≤ 10^5
"""


class Solution:
    def is_array_representing_bst(self, arr):
        """
        For bst the inorder gives sorted, so just checking whether array is sorted or not
        """
        for i in range(1, len(arr)):
            # Checking current value with previous
            if arr[i - 1] > arr[i]:
                return 0

        return 1


def main():
    arr = input("Enter the array: ").strip().split()
    arr = list(map(int, [x.replace(",", "").strip() for x in arr]))
    soln = Solution()
    result = soln.is_array_representing_bst(arr)
    print(result)


if __name__ == "__main__":
    main()
