"""
Given two unsorted integer arrays a[] and b[] each consisting of distinct elements, the task is to return the count of elements in the intersection (or common elements) of the two arrays.

Intersection of two arrays can be defined as the set containing distinct common elements between the two arrays.

Examples:

Input: a[] = [89, 24, 75, 11, 23], b[] = [89, 2, 4]
Output: 1
Explanation: 89 is the only element in the intersection of two arrays.

Input: a[] = [1, 2, 4, 3, 5, 6], b[] = [3, 4, 5, 6, 7]
Output: 4
Explanation: 3, 4, 5, and 6 are the elements in the intersection of two arrays.

Input: a[] = [20, 10, 30, 50, 40], b[] = [15, 25, 30, 20, 35]
Output: 2
Explanation: 20 and 30 are the elements in the intersection of the two arrays.

Constraints:
1  ≤  a.size(), b.size() ≤  10^5
1  ≤  a[i], b[i]  ≤  10^5

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(n)
"""

from collections import defaultdict


class Solution:
    def intersecton_of_arrays_with_distinct(self, arr1, arr2):
        result = 0
        seen_map = defaultdict(int)
        for ele in arr1:
            seen_map[ele] += 1

        for ele in arr2:
            if ele in seen_map:
                result += 1

        return result


def main():
    arr1 = [
        int(value) for value in input("Enter value for first array: ").strip().split()
    ]
    arr2 = [
        int(value) for value in input("Enter value for second array: ").strip().split()
    ]
    solution = Solution()
    print(solution.intersecton_of_arrays_with_distinct(arr1, arr2))


if __name__ == "__main__":
    main()
