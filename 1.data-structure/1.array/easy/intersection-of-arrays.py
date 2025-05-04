"""
Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing.

Examples:

Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
Output: [1, 3]
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.

Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
Output: [1]
Explanation: 1 is the only common element present in both the arrays.

Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
Output: []
Explanation: No common element in both the arrays.

Constraints:
1 ≤ a.size(), b.size() ≤ 10^5
1 ≤ a[i], b[i] ≤ 10^5

Expected Complexities
Time Complexity: O( a.size() + b.size() )
Auxiliary Space: O( a.size() )
"""


class Solution:
    def intersection_array(self, arr1, arr2):
        intersection_array = []
        large_set = set(arr2 if len(arr1) < len(arr2) else arr1)
        small_set = set(arr1 if len(arr1) < len(arr2) else arr2)

        for ele in small_set:
            # Conversion to set for large array to have on average O(1) for in operator
            if ele in large_set:
                intersection_array.append(ele)

        return intersection_array


def main():
    print("Enter first list:")
    arr1 = [int(value) for value in input().strip().split()]
    print("Enter Second list:")
    arr2 = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.intersection_array(arr1, arr2))


if __name__ == "__main__":
    main()
