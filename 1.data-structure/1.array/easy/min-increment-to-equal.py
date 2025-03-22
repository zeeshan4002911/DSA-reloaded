"""
Given an array arr[] and an integer k. You can perform an operation in which you can increment any of the number in the array by k. Find the minimum number of operations needed to make all the elements of array equal.

Note: If it is not possible to make all elements of array equal return -1.

Examples:

Input: arr[] = [4, 4, 4, 2], k = 2
Output: 1
Explanation: We can increment the element at last index of the array by 2 to make all the elements equal to 4.

Input: arr[] = [4, 2, 6, 8], k = 3
Output: -1
Explanation: It can be proven that these elements can't be made equal by applying any number of operations.

Input: arr[] = [4, 7, 19, 16], k = 3
Output: 10

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105
1 <= k <= 104

"""


class Solution:
    def count_operation(self, arr, k):
        """
        1. Max element as target for simplifying calculation
        2. Difference of each element from target divisiblity check by k for feasibility
        3. Count of operation for each element
        """
        max_element = max(arr)

        operations = 0
        for ele in arr:
            if (max_element - ele) % k != 0:
                return -1
            operations += (max_element - ele) // k

        return operations


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter the value of k:", end=" ")
    k = int(input())
    solution = Solution()
    print(solution.count_operation(arr, k))


if __name__ == "__main__":
    main()
