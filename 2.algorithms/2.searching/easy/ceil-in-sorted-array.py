"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the smallest element in arr[] that is greater than or equal to x. This element is called the ceil of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the first occurrence.

Examples

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2.

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], x = 20
Output: -1
Explanation: No element greater than 20 is found. So output is -1.

Input: arr[] = [1, 1, 2, 8, 10, 11, 12, 19], x = 0
Output: 0
Explanation: Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ x ≤ arr[n-1]

Expected Complexities
Time Complexity: O(log n)
Auxiliary Space: O(1)

"""


class Solution:
    # Recursive approach
    def ceil_in_sorted_array(self, arr, x):
        size = len(arr)
        result = -1
        return self.modified_binary_search(arr, 0, size - 1, x, result)

    def modified_binary_search(self, arr, low, high, target, result):
        if low > high:
            return result

        mid = low + (high - low) // 2

        if arr[mid] >= target:
            # Possible answer, but check if there's a smaller index
            return self.modified_binary_search(arr, low, mid - 1, target, mid)
        else:
            return self.modified_binary_search(arr, mid + 1, high, target, result)

    # Iterative approach and similar to in-built bisect_left method of python
    def ceilSearch(arr, x):
        low = 0
        high = len(arr) - 1
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] < x:
                low = mid + 1
            else:
                # Possible answer, but check if there's a smaller index
                result = mid
                high = mid - 1

        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    x = int(input())

    solution = Solution()
    print(solution.modified_binary_search(arr, x))


if __name__ == "__main__":
    main()
