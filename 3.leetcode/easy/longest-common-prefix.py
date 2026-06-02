"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

"""

from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        prefix_res = ""
        size = len(strs)
        if size == 0:
            return prefix_res

        # Outer loop: Iterate for the character of first string
        first_str_size = len(strs[0])
        for i in range(first_str_size):
            j = 0
            # Inner Loop: Iterate for the a specific character in all the strings
            while j < size:
                # First condition for any word smaller than first reference word
                # Second condition when prefix does not match
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return prefix_res
                j += 1

            prefix_res += strs[0][i]

        return prefix_res


def main():
    arr = input("Enter array of string: ").strip()
    arr = arr.replace(",", " ").split()
    soln = Solution()
    print(soln.longest_common_prefix(arr))


if __name__ == "__main__":
    main()
