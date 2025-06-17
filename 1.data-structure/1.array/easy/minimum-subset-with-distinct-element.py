"""
You are given an array of n-element. You have to make subsets from the array such that no subset contain duplicate elements. Find out minimum number of subset possible.

Examples :

    Input : arr[] = {1, 2, 3, 4}
    Output :1
    Explanation : A single subset can contains all values and all values are distinct.

    Input : arr[] = {1, 2, 3, 3}
    Output : 2
    Explanation : We need to create two subsets {1, 2, 3} and {3} [or {1, 3} and {2, 3}] such that both subsets have distinct elements.
"""


class Solution:
    def missing_subset_with_distinct_element(self, arr):
        """
            If all elements are distinct, we need to make only one subset.
            If all elements are same, we need make n subsets.
            If an element appears twice, and all other are distinct, we need to make two subsets.
            If there are multiple elements having duplicate then number of subset should be based on maximum duplicate of a number, other duplicate which is less compare to maximum can be present in subset to have distinct.
        """
        freq_count = {}
        # Storing the number of occurence of element as frequency
        for ele in arr:
            freq_count[ele] = freq_count.get(ele, 0) + 1

        max_freq = max(freq_count.values())
        return max_freq


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.missing_subset_with_distinct_element(arr))


if __name__ == "__main__":
    main()
