"""
Given a sorted array arr[] of n positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.

Examples :

Input: n = 5, arr[] = {1, 1, 2, 5, 5}
Output: 2
Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

Input: n = 7, arr[] = {2, 2, 5, 5, 20, 30, 30}
Output: 20
Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.

Expected Time Complexity: O( Log(n) ).
Expected Auxiliary Space: O(1).

Constraints
0 <  n  <= 10^6
0 <= arr[i] <= 10^9
"""


class Solution:
    def single_element_among_doubles(self, n, arr):
        if n == 0:
            return None
        return self.modified_binary_search(n, arr, 0, n - 1)

    def modified_binary_search(self, n, arr, low, high):
        if low >= high:
            return arr[low]
    
        mid = low + (high - low) // 2

        if (mid - 1 >= 0 and mid + 1 <= n - 1 and  arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]):
            return arr[mid] 
        elif (mid % 2 == 1 and arr[mid] == arr[mid-1]) or (mid % 2 == 0 and arr[mid] == arr[mid+1]):
            """
            In a sorted array where all elements appear exactly twice except one, the unique element will be at the position where the pairing breaks.
            If mid is even and arr[mid] == arr[mid + 1], the unique element is in the right half.
            If mid is odd and arr[mid] == arr[mid - 1], the unique element is in the right half.
            Otherwise, it's in the left half.
            """
            return self.modified_binary_search(n, arr, mid + 1, high)
        else:
            return self.modified_binary_search(n, arr, low, mid - 1)

def main():
    n = int(input())
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.single_element_among_doubles(n, arr))


if __name__ == "__main__":
    main()
