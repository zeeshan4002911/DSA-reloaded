"""
Given a string consisting of lowercase letters, arrange all its letters in ascending order.

Example 1:

Input:
S = "edcab"
Output: "abcde"
Explanation: characters are in ascending
order in "abcde".

Example 2:

Input:
S = "xzy"
Output: "xyz"
Explanation: characters are in ascending
order in "xyz".



Your Task:
You don't need to read input or print anything. Your task is to complete the function sort() which takes the string as inputs and returns the modified string.

Expected Time Complexity: O(|S| * log |S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 10^5
S contains only lowercase alphabets.

"""


class Solution:
    # Using counting sort appraoch (TC: O(n), SC: O(k))
    def sort_string(self, s):
        MAX_CHAR = 26
        charCount = [0] * MAX_CHAR

        # Traverse the string and count characters
        for ch in s:
            charCount[ord(ch) - ord("a")] += 1

        result = ""
        # Traverse the count array and print characters
        for i in range(MAX_CHAR):
            letter = chr(i + ord("a")) * charCount[i]
            result += letter
        return result

    # Using sort method of python (TC: O(n * log(n)), SC: O(n))
    def sort_a_string(self, s):
        arr = [char for char in s]
        arr.sort()
        return "".join(arr)


def main():
    s = str(input())
    solution = Solution()
    print(solution.sort_string(s))


if __name__ == "__main__":
    main()
