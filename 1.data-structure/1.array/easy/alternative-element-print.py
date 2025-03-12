"""
    Input: arr[] = [10, 20, 30, 40, 50]
    Output: 10 30 50
    Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

    Input: arr[] = [-5, 1, 4, 2, 12]
    Output: -5 4 12

"""


def printAlternative(arr):
    n = len(arr)
    for i in range(0, n, 2):
        print(arr[i], end=" ")


if __name__ == "__main__":
    testCases = [[10, 20, 30, 40, 50], [-5, 1, 4, 2, 12]]
    t = 0
    n = len(testCases)
    while t < n:
        printAlternative(testCases[t])
        print()
        t += 1