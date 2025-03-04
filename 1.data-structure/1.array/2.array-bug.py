# Rotate the array A by B positions.

class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        for i in range(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret
    
if __name__ == "__main__":
    sol = Solution()
    A = [1,2,3,4,5,6]
    B = 1
    result = sol.rotateArray(A, B)
    for val in result:
        print(val, end=" ")