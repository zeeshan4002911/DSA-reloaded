"""
Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false.

Examples:

Input: arr[] = [5, 20, 3, 2, 5, 80], x = 78
Output: true
Explanation: Pair (2, 80) have an absolute difference of 78.

Input: arr[] = [90, 70, 20, 80, 50], x = 45
Output: false
Explanation: There is no pair with absolute difference of 45.

Input: arr[] = [1], x = 1
Output: false

Constraints:
1<= arr.size() <= 10^6
1<= arr[i] <= 10^6
0<= x <= 10^5

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(1)

"""


class Solution:
    def two_pair_diff_using_two_pointers(self, arr, x):
        """
        Sort the array then using two pointers approach to find the pair - it's a variant of two pointer
        TC: For sorting O(nlog(n)) + for traversal of array using two pointers O(n) = O(nlog(n))
        SC: O(1)
        """
        arr.sort()
        size = len(arr)
        i = 0
        j = 1
        while i < size and j < size:
            diff = arr[j] - arr[i]
            if i != j and diff == x:
                return True
            elif diff < x:
                j += 1
            else:
                i += 1
        return False

    def two_pair_diff_using_binary_search(self, arr, x):
        """
        Sort the array and then for each element binary search of compliment (x - element) in remaining right portion,
        TC: O(nlog(n)) for sort + O(n) * O(log(n)) for binary search = O(nlog(n)),
        SC: O(1)
        """
        arr.sort()
        size = len(arr)
        for i in range(size):
            low = i + 1
            high = size - 1
            target = x + arr[i]
            result = self.binary_search(arr, low, high, target)
            if result:
                return True
        return False

    def binary_search(self, arr, low, high, target):
        if low > high:
            return False

        mid = low + (high - low) // 2
        if arr[mid] > target:
            return self.binary_search(arr, low, mid - 1, target)
        if arr[mid] < target:
            return self.binary_search(arr, mid + 1, high, target)
        else:
            return True

    def two_pair_diff_using_hashing(self, arr, x):
        seen = set()
        for ele in arr:
            pos_complement_num = ele - x
            neg_complement_num = ele + x
            if pos_complement_num in seen or neg_complement_num in seen:
                return True
            seen.add(ele)
        return False


def main():
    arr = [int(value) for value in input().strip().split()]
    x = int(input())
    solution = Solution()
    print(solution.two_pair_diff_using_two_pointers(arr, x))


if __name__ == "__main__":
    main()
