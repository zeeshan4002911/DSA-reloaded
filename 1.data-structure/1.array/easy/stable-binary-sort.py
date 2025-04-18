"""z
Stable Binary Sort

Given an array arr[] of integers, the task is to partition the array based on even and odd elements. The partition has to be stable, meaning the relative ordering of all even elements must remain the same before and after partitioning, and the same should hold true for all odd elements.

Note: For a binary array (containing only 0s and 1s), this partition process is equivalent to sorting the array.

Examples:

    Input: arr[] = [1, 0, 1, 1, 0, 0]
    Output: [0 ,0 ,0, 1, 1, 1]
    Explanation: All even numbers came before the odd numbers.

    Input: arr[] = [1, 2, 3, 4, 5]
    Output: [2, 4, 1, 3, 5]
    Explanation: All even numbers [2, 4] came before the odd numbers [1, 3, 5], and the relative ordering was also same.

    Input: arr[] = [-5, -2, 0, 4, 7, 9]
    Output: [-2, 0, 4, -5, 7, 9]
    Explanation: All even numbers [-2, 0, 4] came before the odd numbers [-5, 7, 9], and the relative ordering was also same.
"""


class Solution:
    def partition_even_odd(self, arr):
        evens = []
        odds = []

        for ele in arr:
            if ele % 2 == 0:
                evens.append(ele)
            else:
                odds.append(ele)

        evens_size = len(evens)
        for i in range(len(arr)):
            if i < evens_size:
                arr[i] = evens[i]
            else:
                k = i - evens_size
                arr[i] = odds[k]

        return arr


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.partition_even_odd(arr))


if __name__ == "__main__":
    main()
