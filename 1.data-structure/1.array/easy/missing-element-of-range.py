"""
Given an array, arr[0..n-1] of distinct elements and a range [low, high], find all numbers that are in a range, but not the array. The missing elements should be printed in sorted order.

Examples:

    Input: arr[] = {10, 12, 11, 15},
           low = 10, high = 15
    Output: 13, 14

    Input: arr[] = {1, 14, 11, 51, 15},
           low = 50, high = 55
    Output: 50, 52, 53, 54 55
"""


class Solution:
    def missing_element_of_range(self, arr, low, high):
        hash_set = set(arr)
        sorted_list = sorted(hash_set)

        result = []
        for x in range(low, high + 1):
            if x not in sorted_list:
                result.append(x)
        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    low = int(input("Enter start of range: "))
    high = int(input("Enter end of range: "))
    solution = Solution()
    print(solution.missing_element_of_range(arr, low, high))


if __name__ == "__main__":
    main()
