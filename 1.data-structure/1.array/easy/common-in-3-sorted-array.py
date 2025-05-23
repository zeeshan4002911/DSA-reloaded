"""
Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

Note: can you handle the duplicates without using any additional Data Structure?

Examples :

Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [20, 80]
Explanation: 20 and 80 are the only common elements in arr, brr and crr.

Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
Output: [-1]
Explanation: There are no common elements in arr, brr and crr.

Input: arr1 = [1, 1, 1, 2, 2, 2], B = [1, 1, 2, 2, 2], arr3 = [1, 1, 1, 1, 2, 2, 2, 2]
Output: [1, 2]
Explanation: We do not need to consider duplicates

Constraints:
1 <= arr1.size(), arr2.size(), arr3.size() <= 105
-105 <= arr1i , arr2i , 1arr3i <= 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)

"""


class Solution:
    def common_in_3_sorted_array(self, arr1, arr2, arr3):
        result = []
        p1, p2, p3 = 0, 0, 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        while p1 < n1 and p2 < n2 and p3 < n3:
            while p2 < n2 and arr2[p2] < arr1[p1]:
                p2 += 1

            while p3 < n3 and arr3[p3] < arr1[p1]:
                p3 += 1

            if p2 < n2 and p3 < n3 and arr1[p1] == arr2[p2] == arr3[p3]:
                if result == [] or arr1[p1] != result[-1]:
                    result.append(arr1[p1])

            p1 += 1
            
        if len(result) == 0:
            result = -1
        return result


def main():
    arr1 = [int(value) for value in input().strip().split()]
    arr2 = [int(value) for value in input().strip().split()]
    arr3 = [int(value) for value in input().strip().split()]

    solution = Solution()
    print(solution.common_in_3_sorted_array(arr1, arr2, arr3))


if __name__ == "__main__":
    main()
