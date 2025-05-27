"""
Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Note:- You don't have to return the array, you have to modify it in-place.

Example:

Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.

Input: arr[] = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
Explanation: 0 2 4 are even and 1 3 are odd numbers.

Input: arr[] = [10, 22, 4, 6]
Output: [10, 22, 4, 6]
Explanation: Here all elements are even, so no need of segregataion

Constraints:
1 ≤ arr.size() ≤ 10^6
0 ≤ arr[i] <= 10^5

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(1)
"""


class Solution:
    def segregate_even_and_odd(self, arr):
        size = len(arr)
        i = 0
        j = size - 1
        # partitioning using two pointers aka hoare's partition algorithm
        while i < j:
            while arr[i] % 2 == 0 and i < size - 1:
                i += 1

            while arr[j] % 2 == 1 and j > 0:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        # Sorting of even and odd part separately
        arr[:i] = sorted(arr[:i])
        arr[i:] = sorted(arr[i:])
        return arr


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.segregate_even_and_odd(arr))


if __name__ == "__main__":
    main()
