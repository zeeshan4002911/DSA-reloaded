"""
You are given an array arr, you need to find any three elements in it such that arr[i] < arr[j] < arr[k] and i < j < k.

Note:

    The output will be 1 if the subsequence returned by the function is present in the array arr
    If the subsequence is not present in the array then return an empty array, the driver code will print 0.
    If the subsequence returned by the function is not in the format as mentioned then the output will be -1.

Examples :

Input: arr = [1, 2, 1, 1, 3]
Output: 1
Explanation: A subsequence 1 2 3 exist.

Input: arr = [1, 1, 3]
Output: 0
Explanation: No such Subsequence exist, so empty array is returned (the driver code automatically prints 0 in this case).

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 106
"""


class Solution:
    def sorted_subsequence(self, arr):
        if len(arr) < 3:
            return []
        min_value = float("inf")
        first_min_value = min_value
        second_min_value = float("inf")
        third_min_value = float("inf")
        for i in range(len(arr)):
            if arr[i] < min_value:
                min_value = arr[i]
            elif arr[i] < second_min_value and arr[i] > min_value:
                second_min_value = arr[i]
                first_min_value = min_value
            elif arr[i] > second_min_value:
                third_min_value = arr[i]
                return [first_min_value, second_min_value, third_min_value]

        return []


def isSubSequence(arr, sub):
    it = iter(arr)
    return all(elem in it for elem in sub)


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    res = solution.sorted_subsequence(arr)
    if len(res) != 0 and len(res) != 3:
        print(-1)
    else:
        if not res:
            print(0)
        elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
            print(1)
        else:
            print(-1)


if __name__ == "__main__":
    main()
