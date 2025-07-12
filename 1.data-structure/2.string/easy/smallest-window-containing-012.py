"""
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Example 1:

Input:
S = 10212
Output:
3
Explanation:
The substring 102 is the smallest substring
that contains the characters 0, 1 and 2.

Example 2:

Input:
S = 12121
Output:
-1
Explanation:
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.

Your Task:
Complete the function smallestSubstring() which takes the string S as input, and returns the length of the smallest substring of string S that contains all the three characters 0, 1 and 2.

Expected Time Complexity: O( length( S ) )
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ length( S ) ≤ 10^5
All the characters of String S lies in the set {'0', '1', '2'}
"""


class Solution:
    # Sliding window approach
    def smallest_window_containing_0_1_2(self, s):
        size = len(s)
        left, right = 0, 0
        count_map = dict()
        result = float("inf")

        # Dynamic window size change
        while right < size:
            if s[right] not in count_map:
                count_map[s[right]] = 0
            # Increase the window end pointer (right)
            count_map[s[right]] += 1
            right += 1

            # For each window minimize the window by decreasing the start pointer (left)
            while len(count_map) == 3:
                result = min(result, right - left)
                if count_map[s[left]] > 1:
                    count_map[s[left]] -= 1
                else:
                    del count_map[s[left]]
                left += 1

        if result == float("inf"):
            result = -1
        return result


def main():
    s = input()
    solution = Solution()
    print(solution.smallest_window_containing_0_1_2(s))


if __name__ == "__main__":
    main()
