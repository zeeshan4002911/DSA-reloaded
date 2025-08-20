"""
A Tic-Tac-Toe board of size 3X3 is given after all the moves are played, i.e., all nine spots are filled. Find out if the given board is valid, i.e., is it possible to reach this board position after a set of moves or not.
Note that every arbitrarily filled grid of 9 spaces isn’t valid, e.g., a grid filled with 3 X and 6 O isn’t a valid situation because each player needs to take alternate turns.

Note:  The game starts with X

Examples:

Input:
board[] = {'X', 'X', 'O',
           'O', 'O', 'X',
           'X', 'O', 'X'};
Output: Valid
Explanation: This is a valid board.

Input:
board[] = {'O', 'X', 'X',
           'O', 'X', 'X',
           'O', 'O', 'X'};
Output: Invalid
Explanation: Both X and O cannot win.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
Every character on the board can either be 'X' or 'O'.
"""


class Solution:
    def validate_tic_tac_toe(self, mat):
        x_count, o_count = 0, 0

        for row in mat:
            for ele in row:
                if ele == "X":
                    x_count += 1
                else:
                    o_count += 1

        # As, x starts the game based on question and they played one by one in turns
        if x_count != o_count and x_count != o_count + 1:
            return False

        x_win_flag, o_win_flag = False, False
        # Check for row and column wins
        for i in range(3):
            if mat[i][0] == mat[i][1] == mat[i][2]:
                if mat[i][0] == "X":
                    x_win_flag = True
                elif mat[i][0] == "O":
                    o_win_flag = True
            if mat[0][i] == mat[1][i] == mat[2][i]:
                if mat[0][i] == "X":
                    x_win_flag = True
                elif mat[0][i] == "O":
                    o_win_flag = True

        # Check for diagonal wins
        if mat[0][0] == mat[1][1] == mat[2][2]:
            if mat[0][0] == "X":
                x_win_flag = True
            else:
                o_win_flag = True
        if mat[0][2] == mat[1][1] == mat[2][0]:
            if mat[0][2] == "X":
                x_win_flag = True
            else:
                o_win_flag = True

        # Invalid if both X and O have won simultaneously
        if x_win_flag and o_win_flag:
            return False

        # If X wins, it must have one more move than O
        if x_win_flag and x_count != o_count + 1:
            return False

        # If O wins, X and O must have equal moves
        if o_win_flag and x_count != o_count:
            return False

        return True


def main():
    print("Enter the tic tac toe matrix")
    mat = [input().strip().split()[:3] for _ in range(3)]

    solution = Solution()
    print(solution.validate_tic_tac_toe(mat))


if __name__ == "__main__":
    main()
