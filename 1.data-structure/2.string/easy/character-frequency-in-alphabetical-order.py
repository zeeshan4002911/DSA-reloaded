"""
Given a string s, the task is to print the frequency of each of the characters of s in alphabetical order.
Example:

    Input: s = "aabccccddd"
    Output: a2b1c4d3
    Since it is already in alphabetical order, the frequency
    of the characters is returned for each character.

    Input: s = "geeksforgeeks"
    Output: e4f1g2k2o1r1s2

"""


class Solution:
    def character_frequency_in_alphabetical_order(self, s):
        count_arr = [0] * 26
        result = ""

        # Count of occurrence for each character
        for char in s:
            char_ascii = ord(char.lower()) - ord("a")
            if 0 <= char_ascii < 26:
                count_arr[char_ascii] += 1

        # Formation of result in required format
        for i in range(26):
            if count_arr[i] > 0:
                char = chr(ord("a") + i)
                result += char + str(count_arr[i])

        return result


def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.character_frequency_in_alphabetical_order(s))


if __name__ == "__main__":
    main()
