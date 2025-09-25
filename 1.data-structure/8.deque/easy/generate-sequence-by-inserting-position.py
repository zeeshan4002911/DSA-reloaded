"""
Given a string S of length N. The string consists only of letters 'F' and 'B'. The task is to generate a sequence performing some operations such that:

    Consider an integer sequence A that consists of only a 0, i.e. A = (0).
    Now, for each index(i) of the string (1 to N), if S[i] is 'F' add i to the immediate front (i.e. left side) of i-1 in sequence A
    Else if S[i] is 'B' add i to the immediate back (i.e. right side) of i-1 sequence A.
    Print the resultant sequence A.

    Examples :

    Input: N = 5, S = "FBBFB"
    Output: 1 2 4 5 3 0
    Explanation: Initially, A = {0}.
    S[1] is 'F' , sequence becomes {1, 0}
    S[2] is 'B' , sequence becomes {1, 2, 0}
    S[3] is 'B' , sequence becomes {1, 2, 3, 0}
    S[4] is 'F' , sequence becomes {1, 2, 4, 3, 0}
    S[5] is 'B' , sequence becomes {1, 2, 4, 5, 3, 0}

    Input : N = 6 , S = "BBBBBB"
    Output : 0 1 2 3 4 5 6

"""

from collections import deque


class Solution:
    def generate_sequence_by_inserting_position(self, s):
        result = deque()
        n = len(s)
        # Last element to starts with
        result.append(n)

        # To simplify the sequence generation backward iteration is needed
        for i in range(n - 1, -1, -1):
            # The operation becomes reverse as we are coming from back
            if s[i] == "F":
                result.append(i)
            elif s[i] == "B":
                result.appendleft(i)
        
        return list(result)


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.generate_sequence_by_inserting_position(s))


if __name__ == "__main__":
    main()
