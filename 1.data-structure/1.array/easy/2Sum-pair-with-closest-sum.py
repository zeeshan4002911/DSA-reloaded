"""
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.

Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target.

Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.

Constraints:
1 <= arr.size() <= 2*10^5
0 <= target<= 2*10^5
0 <= arr[i] <= 10^5

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(1)
"""


class Solution:
    def two_pair_with_closest_sum(self, arr, target):
        arr.sort()
        left, right = 0, len(arr) - 1
        closness = float("inf")
        result = []

        while left < right:
            local_sum = arr[left] + arr[right]
            
            # Closeness check and update base on condition
            local_closeness = abs(local_sum - target)
            if local_closeness < closness:
                closness = local_closeness
                result = [arr[left], arr[right]]
            
            # Normal two pointers approach
            if local_sum < target:
                left += 1
            elif local_sum > target:
                right -= 1
            else:
                return [arr[left], arr[right]]

        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    target = int(input("Enter the value of target: "))
    solution = Solution()
    print(solution.two_pair_with_closest_sum(arr, target))


if __name__ == "__main__":
    main()
