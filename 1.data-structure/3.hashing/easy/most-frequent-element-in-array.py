"""
You are given an integer array arr[]. You need to return the element which occurs maximum times in arr[].
Note: If multiple such elements exists return the maximum element.

Example:

Input: arr[] = [1, 2, 2, 2, 4, 1]
Output: 2
Explanation: 2 is most frequent element of this array with 3 occurrences.

Input: arr[] = [1, -5, 8, 1]
Output: 1
Explanation: 1 is most frequent element of this array with 2 occurrences.

Input: arr[] = [3, 0, 0, 3, 8]
Output: 3
Explanation: 0 and 3 are two most frequent elements of this array. 3 is the maximum, so 3 is the answer.

Constraints:
1<=arr.size()<=10^5
-10^5<=arr[i]<=10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def most_frequent_element(self, arr):
        count_map = {}
        # Storing the frequency of each occurence of element
        for ele in arr:
            if ele not in count_map:
                count_map[ele] = 1
            else:
                count_map[ele] = count_map[ele] + 1

        # Finding the max element based on max frequency
        max_freq = max(count_map.values())
        max_element = None
        for ele, freq in count_map.items():
            if freq == max_freq:
                if max_element is None:
                    max_element = ele
                else:
                    max_element = max(ele, max_element)

        return max_element


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.most_frequent_element(arr))


if __name__ == "__main__":
    main()
