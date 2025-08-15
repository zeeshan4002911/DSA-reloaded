"""
Given string s containing only lowercase characters, the task is to print the characters along with their frequency in the order of their occurrence and in the given format explained in the examples below.

Examples:

    Input: s = "geeksforgeeks"
    Output: g2 e4 k2 s2 f1 o1 r1

    Input: str = "elephant"
    Output: e2 l1 p1 h1 a1 n1 t1

"""


class Solution:
    def character_frequency_in_order_of_occurrence(self, s):
        count_map = {}
        result = ""
        
        # Count of occurrence for each character
        for char in s:
            if char in count_map:
                count_map[char] += 1
            else:
                count_map[char] = 1

        # Formation of result in required format
        for char in s:
            if count_map[char] > 0:
                result += char + str(count_map[char]) + " "
                # Marking with 0 to avoid adding duplication in result
                count_map[char] = 0
        
        # Removal of last extra space
        result = result[:-1]
        return result


def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.character_frequency_in_order_of_occurrence(s))


if __name__ == "__main__":
    main()
