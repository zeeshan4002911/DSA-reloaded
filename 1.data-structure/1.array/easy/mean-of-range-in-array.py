"""
Given an array arr and q queries. Write a program to find the floor value of the mean in the range l to r for each query in a new line.
Queries are given by an array of queries[] of size 2*q. Here queries[2*i] denote l and queries[2*i+1] denote r for i-th query.

Examples:

Input : arr[] = [1, 2, 3, 4, 5] and q[] = [0, 2, 1, 3, 0, 4]
Output : [2, 3, 3]
Explanation: Here we can see that the array of integers is [1, 2, 3, 4, 5]. Query 1: L = 0 and R = 2 Sum = 6 Integer Count = 3 So, Mean is 2

Input : arr[] = [6, 7, 8, 10] and q[] = [0, 3, 1, 2]
Output : [7, 7]
Explanation: Element count is 3 and sum of element from 0 to 3 are 21. So mean is 7.

Expected Time Complexity: O(q + n).
Expected Auxiliary Space: O(n).

Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^3
"""


class Solution:
    def mean_of_range_in_array(self, arr, q):
        size = len(arr)
        result = []

        # Prefix Sum Array creation commute the sum for each query in constant time
        prefix_sum_arr = [None] * size
        prefix_sum_arr[0] = arr[0]
        for i in range(1, size):
            prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i]

        # Generating sum for each query
        for i in range(len(q) // 2):
            l = q[2 * i]
            r = q[2 * i + 1]
            """ 
            In case left of range is not on first index then subtracting the right with left - 1 of prefix sum array to have sum including the left index element
            """
            if l != 0:
                local_sum = prefix_sum_arr[r] - prefix_sum_arr[l - 1]
            else:
                # In case of left range on first index the prefix sum
                local_sum = prefix_sum_arr[r]

            # Number of elements between l and r range
            numbers_in_range = r - l + 1
            result.append(local_sum // numbers_in_range)

        return result


def main():
    arr = [int(val) for val in input("Input list: ").strip().split()]
    q = [int(val) for val in input("Input queries(q): ").strip().split()]
    solution = Solution()
    print(solution.mean_of_range_in_array(arr, q))


if __name__ == "__main__":
    main()
