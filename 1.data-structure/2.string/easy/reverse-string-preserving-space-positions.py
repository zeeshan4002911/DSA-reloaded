"""
Given a string, your task is to reverse the string keeping the spaces intact to their positions.

Example 1:

Input:
S = "Help others"
Output: sreh topleH
Explanation: The space is intact at index 4
while all other characters are reversed.

Example 2:

Input:
S = "geeksforgeeks"
Output: skeegrofskeeg
Explanation: No space present, hence the
entire string is reversed.


Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseWithSpacesIntact() which takes the string S as input and returns the resultant string by reversing the string while keeping all the spaces intact.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=105
"""


class Solution:
    def reverse_string_spaces_intact(self, s):
        s_arr = list(s)
        left, right = 0, len(s_arr) - 1
        # 2-pointers method
        while left < right:
            if s_arr[left] != " " and s_arr[right] != " ":
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                
            if s_arr[left] == " ":
                left += 1
            elif s_arr[right] == " ":
                right -= 1
            else:
                left += 1
                right -= 1
        return str("").join(s_arr)


def main():
    s = input()
    solution = Solution()
    print(solution.reverse_string_spaces_intact(s))


if __name__ == "__main__":
    main()
