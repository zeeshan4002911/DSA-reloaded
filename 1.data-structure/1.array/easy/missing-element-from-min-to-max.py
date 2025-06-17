"""
Given an integer array arr[], the task is to find how many elements should be added such that all elements between the maximum element and minimum element are present in the array.

Examples:

Input: arr[] = [205, 173, 102, 324, 957]
Output: 851
Explanation: The maximum element is 957 and the minimum element is 102. Total elements from 102 to 957 = 854, out of which 3 are already present. So answer is 851.

Input: arr[] = [3, 4, 4, 8]
Output: 3
Explanation: The maximum element is 8 and the minimum element is 3. Total elements from 3 to 8 = 6, out of which 3 are already present. So, answer is 3.

Input: arr[] = [545]
Output: 0
Explanation: We don't need to add any elements to the array.

Constraints:
1 <= arr.size() <= 10^5
1 <= arr[i] <= 10^9

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def missing_element_from_min_to_max(self, arr):
        non_duplicate_set = set(arr)
        min_ele = min(arr)
        max_ele = max(arr)

        # Total number of elements which should be present within range, +1 to include minimum number
        expected_total = max_ele - min_ele + 1
        # Actual non duplicate total numbers present in input
        actual_total = len(non_duplicate_set)
        missing_ele = expected_total - actual_total
        return missing_ele


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.missing_element_from_min_to_max(arr))


if __name__ == "__main__":
    main()
