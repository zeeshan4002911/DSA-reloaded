"""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

    Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.

Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2.

Constraints:
1  <=  a.size(), b.size()  <=  10^5
-109  <=  a[i] , b[i]  <=  10^9

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(1)
"""


class Solution:
    def union_sorted_array(self, arr1, arr2):
        # Using merge sort combine approach
        '''
        Note: These below are not bitwise operator but short-hand in python for .union() and .intersection() method
            Union -> sorted(list(set(arr1) | set(arr2)))
            Intersection -> sorted(list(set(arr1) & set(arr2)))
        '''
        result = []
        i = j = 0
        n = len(arr1)
        m = len(arr2)

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not result or arr1[i] != result[-1]:
                    result.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not result or arr2[j] != result[-1]:
                    result.append(arr2[j])
                j += 1
            else:
                if not result or arr1[i] != result[-1]:
                    result.append(arr1[i])
                i += 1
                j += 1

        while i < n:
            if not result or arr1[i] != result[-1]:
                result.append(arr1[i])
            i += 1

        while j < m:
            if not result or arr2[j] != result[-1]:
                result.append(arr2[j])
            j += 1

        return result


def main():
    print("Enter first list:")
    arr1 = [int(value) for value in input().strip().split()]
    print("Enter Second list:")
    arr2 = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.union_sorted_array(arr1, arr2))


if __name__ == "__main__":
    main()
