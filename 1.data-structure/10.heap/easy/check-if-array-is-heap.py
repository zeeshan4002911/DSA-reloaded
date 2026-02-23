"""
Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.

Example 1:

Input:
n = 6
arr[] = {90, 15, 10, 7, 12, 2}
Output: 
1
Explanation: 
The given array represents below tree
       90
     /    \
   15      10
  /  \     /
7    12  2
The tree follows max-heap property as every
node is greater than all of its descendants.

Example 2:

Input:  
n = 6
arr[] = {9, 15, 10, 7, 12, 11}
Output:
0
Explanation:
The given array represents below tree
       9
     /    \
   15      10
  /  \     /
7    12  11
The tree doesn't follows max-heap property 9 is
smaller than 15 and 10, and 10 is smaller than 11. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function isMaxHeap() which takes the array arr[] and its size n as inputs and returns True if the given array could represent a valid level order representation of a Max Heap, or else, it will return False.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 10^5
1 ≤ arri ≤ 10^5
"""


class Solution:
    def does_array_represent_heap(self, arr, n):
        # In a complete binary tree last n // 2 nodes are leaf
        last_non_leaf = (n // 2) - 1

        # Checking for all the non leaf value greater than it's child values
        for i in range(last_non_leaf + 1):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if (left_child < n and arr[i] < arr[left_child]) or \
            (right_child < n and arr[i] < arr[right_child]):
                return False

        return True


def main():
    arr = input("Enter array: ").strip().split()
    soln = Solution()
    print(soln.does_array_represent_heap(arr, len(arr)))


if __name__ == "__main__":
    main()
