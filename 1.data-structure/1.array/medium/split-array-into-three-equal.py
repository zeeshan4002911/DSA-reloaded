"""
Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false.

Examples :

Input:  arr[] = [1, 3, 4, 0, 4]
                 i, j
Output: true
Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4, so driver code prints true.

Input: arr[] = [2, 3, 4]
Output: false
Explanation: No three subarrays exist which have equal sum.

Input: arr[] = [0, 1, 1]
Output: false

Constraints:
3 ≤ arr.size() ≤ 10^6
0 ≤ arr[i] ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def split_into_three_equal(self, arr):
        i = 0
        j = 1
        n = len(arr)

        # Based on sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1])
        first_sum = arr[i]
        second_sum = arr[j]
        third_sum = 0

        for r in range(j + 1, n):
            third_sum += arr[r]
    
        # Moving the pointers based on the fact that i < j < n
        while i < j and j < n:
            # Flag to detect pointer position change
            is_pointers_moved = False

            # In case first arr sum is small then moving i pointer
            if first_sum < second_sum:
                i += 1
                is_pointers_moved = True
                first_sum += arr[i]
                second_sum -= arr[i]

            # In case second arr sum is small then moving j pointer
            if second_sum < third_sum:
                j += 1
                is_pointers_moved = True
                second_sum += arr[j]
                third_sum -= arr[j]

            # If no pointer is getting moved then breaking the loop as we either found a value or 
            # it's not possible to split in three equal sum parts
            if not is_pointers_moved:
                break

        if first_sum == second_sum == third_sum:
            return [i, j]

        return [-1, -1]


def main():
    arr = input("Enter the arr: ")
    arr = arr.strip().split()
    arr = [int(val.split(",")[0]) for val in arr]
    soln = Solution()
    res = soln.split_into_three_equal(arr)
    print(res)


if __name__ == "__main__":
    main()
