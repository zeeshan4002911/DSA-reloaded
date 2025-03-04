# Rotate the array A by B positions.


def performOps(A):
    blen = 2 * len(A)
    B = [0] * blen
    for i in range(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    B = performOps(A)
    for val in B:
        print(val, end=" ")
