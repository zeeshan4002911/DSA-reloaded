"""
Given an array arr and an element k. The task is to find the count of elements in the array that appear more than n/k times and n is length of arr.

Examples :

Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times.

Input: arr = [2, 3, 3, 2], k = 3
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.

Input: arr = [1, 4, 7, 7], k = 2
Output: 0
Explanation: In the given array, no element appears more than n/k times.

Constraints:
1 <= arr.size() <= 10^6
0 <= arr[i] <= 10^8
1 <= k <= arr.size()

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def count_occurences(self, arr, k):
        hash_map = dict()
        n = len(arr)
        number_of_occurence = n // k

        # Storing the number of occurence of each element in hashmap
        for ele in arr:
            if ele not in hash_map:
                hash_map[ele] = 1
            else:
                hash_map[ele] = hash_map[ele] + 1

        # Counting the number of elements which has occurence more than n / k
        elements_count = 0
        for value in hash_map.values():
            if value > number_of_occurence:
                elements_count += 1

        return elements_count


def main():
    arr = [int(value) for value in input().strip().split()]
    k = int(
        input(
            "Enter a value of k: ",
        )
    )
    solution = Solution()
    print(solution.count_occurences(arr, k))


if __name__ == "__main__":
    main()
