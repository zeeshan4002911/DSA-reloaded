"""
Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

Note:- The position you return should be according to 1-based indexing.

Examples:

Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
Output: 2
Explanation: 5 appears twice and its first appearance is at index 2 which is less than 3 whose first the occurring index is 3.

Input: arr[] = [1, 2, 3, 4]
Output: -1
Explanation: All elements appear only once so answer is -1.

Constraints:
1 <= arr.size <= 10^6
0 <= arr[i]<= 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)

"""


class Solution:
    def first_repeated(self, arr):
        # Counting sort or pigeon hole sort approach
        size = len(arr)
        max_num = max(arr)
        count_buncket = [0] * (max_num + 1)
        for ele in arr:
            count_buncket[ele] += 1

        for i in range(size):
            if count_buncket[arr[i]] > 1:
                return i + 1
        return -1

    # Recommended approach as average space complexity will be less compare to counting sort appraoch
    def first_repeated_using_set(self, arr):
        seen = set()
        min_num = float("inf")
        # Iterate from end to return the 1 based index from the begining
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] in seen:
                min_num = min(min_num, i)
            seen.add(arr[i])
        if min_num == float("inf"):
            return -1
        else:
            return min_num + 1


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.first_repeated(arr))


if __name__ == "__main__":
    main()
