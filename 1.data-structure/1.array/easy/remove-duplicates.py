"""
Given an array arr consisting of positive integer numbers, remove all duplicate numbers.

Example:

Input: arr[] = [2, 2, 3, 3, 7, 5]
Output: [2, 3, 7, 5]
Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.

Input: arr[] = [2, 2, 5, 5, 7, 7]
Output: [2, 5, 7]

Input: arr[] = [8, 7]
Output: [8, 7]

Constraints:
1<= arr.size() <=106
2<= arr[i] <=100

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def remove_duplicate(self, arr):
        """There is no feasible way to remove duplicate with constant space and linear time complexity
        Note: By using insertion sort on best case time complexity linear time complexity can be achieved but the
        order of elements will get changed due to sorting
        """
        size = len(arr)
        count_arr = [0] * 100
        # Stroing the count for pigeonhole or counting sort alogrithm
        for i in range(size):
            count_arr[arr[i]] += 1

        k = 0
        for i in range(size):
            # Iterate over input instead of count for preserving the order
            while count_arr[arr[i]] > 0:
                if count_arr[arr[i]] == 1:
                    arr[k] = arr[i]
                    k += 1
                count_arr[arr[i]] -= 1

        return arr[:k]


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    result = solution.remove_duplicate(arr)
    print(result)


if __name__ == "__main__":
    main()
