"""
Given a chess board of dimension m * n. Find number of possible moves where knight can be moved on a chessboard from given position. If mat[i][j] = 1 then the block is filled by something else, otherwise empty. Assume that board consist of all pieces of same color, i.e., there are no blocks being attacked.

Examples:

Input : mat[][] = {{1, 0, 1, 0},
                   {0, 1, 1, 1},
                   {1, 1, 0, 1},
                   {0, 1, 1, 1}}
        pos = (2, 2)
Output : 4
Knight can moved from (2, 2) to (0, 1), (0, 3),
(1, 0) and (3, 0).

We can observe that knight on a chessboard moves either:

    Two moves horizontal and one move vertical
    Two moves vertical and one move horizontal

The idea is to store all possible moves of knight and then count the number of valid moves. A move will be invalid if:

    A block is already occupied by another piece.
    Move is out of the chessboard.
"""


class Solution:
    def possible_moves_of_knight(self, mat, pos):
        row = len(mat)
        col = len(mat[0])
        result = []

        # List of all possible moves (8 moves for a knight)
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        # Check all possible moves
        for move in knight_moves:
            new_row = pos[0] + move[0]
            new_col = pos[1] + move[1]

            # Checking if new position is within boundary and is empty (0)
            if 0 <= new_row < row and 0 <= new_col < col and mat[new_row][new_col] == 0:
                result.append((new_row, new_col))

        return len(result)


def main():
    n = int(input("Enter the row: ").strip())
    m = int(input("Enter the column: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:m] for _ in range(n)]
    pos = list(
        map(int, input("Enter the initial position of knight: ").strip().split())
    )[:2]

    solution = Solution()
    print(solution.possible_moves_of_knight(mat, pos))


if __name__ == "__main__":
    main()
