"""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the intersection of the two arrays in sorted order.

    Intersection of two arrays can be defined as the set containing distinct common elements that are present in both of the arrays.

Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3
Explanation: Distinct elements in both the arrays are: 1 2 3.

Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 2 3 4
Explanation: Distinct elements in both the arrays are: 2 3 4.

Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: []
Explanation: No common elements.

Constraints:
1  <=  a.size(), b.size()  <=  10^5
-109  <=  a[i] , b[i]  <=  10^9

Time Complexity: O(n + m)
Auxiliary Space: O(n)
"""


class Solution:
    def intersection_sorted_array(self, arr1, arr2):
        # Using merge sort combine approach
        """
        Note: These below are not bitwise operator but short-hand in python for .union() and .intersection() method
            Union -> sorted(list(set(arr1) | set(arr2)))
            Intersection -> sorted(list(set(arr1) & set(arr2)))
        """
        result = []
        i = j = 0
        n = len(arr1)
        m = len(arr2)

        while i < n and j < m:
            if i > 0 and arr1[i] == arr1[i - 1]:
                i += 1
                continue

            if j > 0 and arr2[j] == arr2[j - 1]:
                j += 1
                continue

            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1

        return result


def main():
    print("Enter first list:")
    arr1 = [int(value) for value in input().strip().split()]
    print("Enter Second list:")
    arr2 = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.intersection_sorted_array(arr1, arr2))


if __name__ == "__main__":
    main()
