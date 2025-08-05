"""
Given two strings txt and pat, return the 0-based index of the first occurrence of the substring pat in txt. If pat is not found, return -1.
Note: You are not allowed to use the inbuilt function.

Examples :

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.

Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: "For" is present as substring in "GeeksForGeeks" from index 5 (0 based indexing).

Input: txt = "GeeksForGeeks", pat = "gr"
Output: -1
Explanation: "gr" is not present in the string "GeeksForGeeks" as substring.

Constraints:
1 ≤ txt.size(),pat.size() ≤ 1000

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""


class Solution:
    def first_occurence(self, txt, pat):
        txt_size = len(txt)
        pat_size = len(pat)

        for i in range(0, txt_size - pat_size + 1):
            """
            # Using in-built method
            if txt[i : i + pat_size] == pat:
                return i
            """
            for j in range(pat_size + 1):
                if j == pat_size:
                    # Result as start index on complete match of charachter of txt and pat
                    return i
                elif txt[i + j] != pat[j]:
                    break

        return -1


def main():
    txt = input("Enter the txt: ").strip()
    pat = input("Enter the pat: ").strip()
    solution = Solution()
    print(solution.first_occurence(txt, pat))


if __name__ == "__main__":
    main()
