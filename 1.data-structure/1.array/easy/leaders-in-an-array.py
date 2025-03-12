"""
Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

    Input: arr[] = [16, 17, 4, 3, 5, 2]
    Output: [17 5 2]
    Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

    Input: arr[] = [1, 2, 3, 4, 5, 2]
    Output: [5 2]
    Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 106
"""


class Solution:
    def leadersInArray(self, arr):
        n = len(arr)
        max = -1
        result = []
        for i in range(n - 1, -1, -1):
            if arr[i] >= max:
                max = arr[i]
                result.append(max)

        # Reverse of the result
        left = 0
        right = len(result) - 1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.leadersInArray(arr))


if __name__ == "__main__":
    main()
