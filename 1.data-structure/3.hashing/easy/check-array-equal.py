"""
Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.

    Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

Examples:

Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
Output: true
Explanation: Both the array can be rearranged to [0,1,2,4,5]

Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
Output: false
Explanation: a[] and b[] have only one common value.

Constraints:
1<= a.size(), b.size()<=10^7
0<=a[i], b[i]<=10^9
Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def check_array_equal(self, arr1, arr2):
        hash_map = {}
        m, n = len(arr1), len(arr2)

        # Array length should be same for equality
        if m != n:
            return False

        for i in range(n):
            # Storing the count of element of both the arrays using dict getter with default value 0
            hash_map[arr1[i]] = hash_map.get(arr1[i], 0) + 1
            hash_map[arr2[i]] = hash_map.get(arr2[i], 0) - 1
            # Deletion of key once it is present in both array and get balanced to 0
            if arr1[i] in hash_map and hash_map[arr1[i]] == 0:
                del hash_map[arr1[i]]
            if arr2[i] in hash_map and hash_map[arr2[i]] == 0:
                del hash_map[arr2[i]]
        
        # In case of unequal arrays hash_map will contain keys with some negative or positive integer value 
        return True if len(hash_map.keys()) == 0 else False


def main():
    arr1 = input().strip().split()
    arr2 = input().strip().split()
    solution = Solution()
    print(solution.check_array_equal(arr1, arr2))


if __name__ == "__main__":
    main()
