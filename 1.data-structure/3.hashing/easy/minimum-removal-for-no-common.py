"""
Given two arrays arr1[] and arr2[], the task is to find the minimum number of elements to remove from each array such that no common elements exist between the two arrays.

Examples:

Input: arr1[] = [2, 3, 4, 5, 8], arr2[] = [1, 2, 3, 4]
Output: 3
Explanation: To remove all common elements, we need to delete 2, 3, and 4 from either array.

Input: arr1[] = [1, 2, 3, 4], arr2[] = [5, 6, 7]
Output: 0
Explanation: There are no common elements between the arrays.

Expected Time Complexity: O(n + m)
Expected Auxiliary Space: O(n + m)

Constraints:
1 ≤ arr1.size(), arr2.size() ≤ 5*105
1 ≤ arr1[i], arr2[i] ≤ 105

"""

class Solution:
    def remove_minimum_number_of_elements(self, arr1, arr2):
        freq_arr1 = {}
        freq_arr2 = {}
        
        for ele in arr1:
            freq_arr1[ele] = freq_arr1.get(ele, 0) + 1
        for ele in arr2:
            freq_arr2[ele] = freq_arr2.get(ele, 0) + 1
        
        result = 0
        for ele in freq_arr1:
            if ele in freq_arr2:
                result += min(freq_arr1[ele], freq_arr2[ele])
        return result


def main():
    arr1 = [int(value) for value in input().strip().split()]
    arr2 = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.remove_minimum_number_of_elements(arr1, arr2))


if __name__ == "__main__":
    main()