"""
Given a string, find the number of pairs of characters that are same. Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered different.

Example 1:

Input:
S = "air"
Output: 3
Explanation: 3 pairs that are equal:
(S[0], S[0]), (S[1], S[1]) and (S[2], S[2])

â€‹Example 2:

Input: 
S = "aa"
Output: 4
Explanation: 4 pairs that are equal:
(S[0], S[0]), (S[0], S[1]), (S[1], S[0])
and (S[1], S[1])


Your Task:
You don't need to read input or print anything. Your task is to complete the function equalPairs() which takes the string S as input and returns the number of equal pairs as described in the problem description.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=10^5
"""

class Solution:
    def count_number_of_equal_pairs(self, s):
        count_arr = [0] * 26
        
        # Counting the occurrence of each character of string
        for char in s:
            char_ascii = ord(char.lower()) - ord('a')
            if 0 <= char_ascii < 26:
                count_arr[char_ascii] += 1
        
        result = 0
        # Calculation of pairs using occurence ^ 2
        for count in count_arr:
            result += count ** 2
        return result


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.count_number_of_equal_pairs(s))


if __name__ == "__main__":
    main()