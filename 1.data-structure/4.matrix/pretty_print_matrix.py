from typing import List


def pretty_print_matrix(mat: List[List]) -> None:
    print("Matrix prettify")
    for row in mat:
        for ele in row:
            print(ele, end=" ")
        print("")
