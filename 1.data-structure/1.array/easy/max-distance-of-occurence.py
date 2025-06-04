"""
Given an array arr[], the task is to find the maximum distance between two occurrences of an element. If no element has two occurrences, then return 0.

Examples:

Input: arr[] = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

Input: arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.

Input: arr[] = [1, 2, 3, 6, 5, 4]
Output: 0
Explanation: No element has two occurrences, so maximum distance = 0.

Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= arr.size() <= 10^6
1 <= arr[i] <= 10^9
"""


class Solution:
    def max_distance_between_same_element(self, arr):
        # For storing track of element position in array as {element: [initial, final]}
        hash_map = {}
        for i, ele in enumerate(arr):
            if ele in hash_map:
                hash_map[ele][1] = i
            else:
                hash_map[ele] = [i, 0]

        # Calculation of distance by comparing max distance with result of substraction of inital from final for each element of array
        max_distance = 0
        for ele in hash_map:
            local_distance = hash_map[ele][1] - hash_map[ele][0]
            max_distance = max(max_distance, local_distance)

        return max_distance


def main():
    arr = input().strip().split()
    solution = Solution()
    print(solution.max_distance_between_same_element(arr))


if __name__ == "__main__":
    main()
