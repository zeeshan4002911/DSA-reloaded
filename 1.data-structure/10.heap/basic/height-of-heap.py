"""
Given a Binary Heap of size n in an array arr[]. Write a program to calculate the height of the Heap.

Note: Return 1 if the n is 1.

Examples:

Input: n = 6, arr[] = [1, 3, 6, 5, 9, 8]
Output: 2
Explaination: The tree is like the following
        (1)
       /   \
    (3)    (6)
    / \     /
  (5) (9) (8)


Input: n = 9, arr[] = [3, 6, 9, 2, 15, 10, 14, 5, 12]
Output: 3
Explaination: The tree looks like following
           (2)
        /      \
      (3)      (9)
     /  \     /   \
   (5) (15) (10) (14)
   / \
 (6) (12)

Constraints:
1 ≤ n ≤ 10^4
1 ≤ arr[i] ≤ 10^6

Expected Complexities
Time Complexity: O(log n)
Auxiliary Space: O(1)
"""

import math


class Solution:
    def heap_height(self, n, arr):
        if n == 1:
            return 1
        return math.floor(math.log2(n))

    def heap_height_calc(self, n, arr):
        if n == 1:
            return 1

        height = 0
        # Starting from root (Can be given any node to calculate height of it)
        current_index = 0

        i = 2 * current_index + 1
        # Keep moving to the left child until we exceed the heap size
        while i < n:
            i = 2 * i + 1
            height += 1

        return height


def main():
    arr = input("Enter array: ").strip().replace(",", " ").split()
    arr = [int(val) for val in arr]

    soln = Solution()
    print(soln.heap_height(len(arr), arr))
    print(soln.heap_height_calc(len(arr), arr))


if __name__ == "__main__":
    main()
