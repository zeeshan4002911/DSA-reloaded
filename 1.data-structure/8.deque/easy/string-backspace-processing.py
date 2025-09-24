"""
Given a string S containing letters and '#'. The '#" represents a backspace. The task is to print the new string without '#'.

Examples:

Input : S = "abc#de#f#ghi#jklmn#op#"
Output : abdghjklmo

Input : S = "##geeks##for##geeks#"
Output : geefgeek

"""

from collections import deque


class Solution:
    def process_backspace(self, s):
        # Stack can be used as well for LIFO property
        result_deque = deque()
        
        for ch in s:
            # Removing the charachter from rear on backspace encounter
            if ch == "#" and result_deque:
                result_deque.pop()
            else:
                result_deque.append(ch)
        
        # String conversion from deque
        result_s = ""
        while result_deque:
            result_s += result_deque.popleft()
        
        return result_s


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.process_backspace(s))


if __name__ == "__main__":
    main()
