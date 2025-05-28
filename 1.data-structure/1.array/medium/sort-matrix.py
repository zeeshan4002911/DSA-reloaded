"""
Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45]
[27,29,37,48]
[32,33,39,50]]
Output:
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.

Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.


Expected Time Complexity:O(N^2LogN)
Expected Auxillary Space:O(N^2)


Constraints:
1 <= N <= 1000
1 <= Mat[i][j] <= 10^5
"""

# from typing import List


class Solution:
    def __get_val(self, index, mat, cols):
        row, col = divmod(index, cols)
        return mat[row][col]

    def __set_val(self, index, value, mat, cols):
        row, col = divmod(index, cols)
        mat[row][col] = value

    def __swap(self, i, j, mat, cols):
        temp = self.__get_val(i, mat, cols)
        self.__set_val(i, self.__get_val(j, mat, cols), mat, cols)
        self.__set_val(j, temp, mat, cols)

    # sort by flattning the matrix [ TC: O(n^2 x Log(n)), SC: O(n ^ 2)]
    def sort_matrix_flatten(self, mat, rows, cols):
        flatten_mat = []
        for i in range(rows):
            for j in range(cols):
                flatten_mat.append(mat[i][j])
        flatten_mat.sort()
        k = 0
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = flatten_mat[k]
                k += 1
        return mat

    # Bubble sort [TC: O(n) ^ 2, SC: O(1)]
    def matrix_bubble_sort(self, mat, rows, cols) -> list[list[int]]:
        size = n = rows * cols
        # Bubble sort using index mapping (pushing greatest number to end on each iteration)
        for i in range(size):
            for j in range(size - 1):
                if self.__get_val(j, mat, cols) > self.__get_val(j + 1, mat, cols):
                    # swap if next index value is smaller
                    self.__swap(j, j + 1, mat, cols)
        return mat

    # Quick Sort [TC: 𝜃(n x log (n), O(n^2), SC: 𝜃(log(n)), O(n)]
    def matrix_quick_sort(self, mat, rows, cols) -> list[list[int]]:
        size = n = rows * cols
        self.matrix_quick_sort_helper(0, size - 1, mat, cols)
        return mat

    def matrix_quick_sort_helper(self, low, high, mat, cols):
        if low >= high:
            return None
        pivot_idx = self.matrix_quick_sort_partition(low, high, mat, cols)
        self.matrix_quick_sort_helper(low, pivot_idx - 1, mat, cols)
        self.matrix_quick_sort_helper(pivot_idx + 1, high, mat, cols)

    def matrix_quick_sort_partition(self, low, high, mat, cols):
        pivot = self.__get_val(high, mat, cols)
        i = low - 1
        for j in range(low, high):
            if self.__get_val(j, mat, cols) <= pivot:
                i += 1
                self.__swap(i, j, mat, cols)
        self.__swap(i + 1, high, mat, cols)
        return i + 1


def pretty_print_matrix(mat: list[list[int]]) -> None:
    print("Matrix prettify")
    for row in mat:
        for ele in row:
            print(ele, end=" ")
        print("")


def main():
    m = int(input("Enter the Number of rows of matrix: "))
    n = int(input("Enter the Number of column of matrix: "))
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(m)]
    solution = Solution()
    pretty_print_matrix(solution.sort_matrix_flatten(mat, m, n))


if __name__ == "__main__":
    main()
