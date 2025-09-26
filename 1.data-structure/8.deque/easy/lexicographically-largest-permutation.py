"""
Given an array arr[] of size n, the task is to find the lexicographically largest permutation by sequentially inserting the array elements to the front or the back of another array which is to be considered initially empty.

Examples:

    Input: arr[] = [3, 1, 2, 4]
    Output: 4 3 1 2
    Explanation:
    The permutations that can be created by sequentially inserting the array elements to the front or the back of the container are {3, 1, 2, 4}, {1, 3, 2, 4}, {2, 3, 1, 4}, {2, 1, 3, 4}, {4, 1, 3, 2}, {4, 2, 3, 1}, {4, 2, 1, 3}, and {4, 3, 1, 2}. Out of which {4, 3, 1, 2} is the lexicographically largest permutation.

    Input: arr[] = [1, 2, 3, 4, 5]
    Output: 5 4 3 2 1
"""

from collections import deque


class Solution:
    def lexicographically_largest_permutation(self, arr):
        size = len(arr)
        result_deque = deque()
        if size >= 1:
            result_deque.append(arr[0])

        # Greedy Approach for maximization
        for i in range(1, size):
            # If element is greater than the front of element result then adding in the front
            if arr[i] >= result_deque[0]:
                result_deque.appendleft(arr[i])
            # For smaller than rear element adding in the rear
            else:
                result_deque.append(arr[i])

        return list(result_deque)


def main():
    arr = input("Enter the Array: ").strip().split()
    solution = Solution()
    print(solution.lexicographically_largest_permutation(arr))


if __name__ == "__main__":
    main()
