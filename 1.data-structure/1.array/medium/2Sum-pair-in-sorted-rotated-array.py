"""
Given an array of positive elements arr[] that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with sum equals to a given target.

Examples:

Input: arr[] = [7, 9, 1, 3, 5], target = 6
Output: true
Explanation: arr[2] and arr[4] has sum equals to 6 which is equal to the target.

Input: arr[] = [2, 3, 4, 1], target = 3
Output: true
Explanation: arr[0] and arr[3] has sum equals to 3 which is equal to the target.

Input: arr[] = [10, 7, 4, 1], target = 9
Output: false
Explanation: There is no such pair exists in arr[] which sums to target.

Constraints:
2 <= arr.size() <=10^6
1 <= arr[i] <= 10^6
1 <= target <= 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def pair_in_sorted_rotated_array_modified(self, arr, target):
        size = len(arr)
        pivot = 0
        for i in range(1, size):
            if arr[i] < arr[i - 1]:
                pivot = i
                break
        
        # The largest number will be the element before pivot
        # Note: Modulo of size is for getting the correct index in case of rotated array
        right = (pivot - 1) % size
        # The smallest number will be the pivot element
        left = pivot
        while left != right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                # Increment of left by 1
                left = (left + 1) % size
            else:
                # Decrement of right by 1
                right = (right - 1) % size
        return False

    def pair_in_sorted_rotated_array(self, arr, target):
        size = len(arr)
        pivot = 0
        for i in range(1, size):
            if arr[i] < arr[i - 1]:
                pivot = i
                break
        # Check for rotation on pivot
        if pivot != 0:
            # Triple reversal technique
            self.reverse(arr, 0, pivot - 1)
            self.reverse(arr, pivot, size - 1)
            self.reverse(arr, 0, size - 1)

        # 2-pointer method for finding the target sum - similar to 2Sum problem
        left, right = 0, size - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


def main():
    arr = list(map(int, input().strip().split()))
    target = int(input("Enter target sum: "))
    solution = Solution()
    print(solution.pair_in_sorted_rotated_array_modified(arr, target))


if __name__ == "__main__":
    main()
