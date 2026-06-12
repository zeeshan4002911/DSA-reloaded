"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"



Constraints:

    1 <= a.length, b.length <= 10^4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_size, b_size = len(a), len(b)
        i, j = a_size - 1, b_size - 1

        # Start of the sum from back side
        carry_forward = 0
        sum_result = []
        while i >= 0 or j >= 0:
            # Number casting and pad with 0
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0
            res, carry_forward = self.unit_sum(num1, num2, carry_forward)
            sum_result.append(res)
            i -= 1
            j -= 1

        if carry_forward == 1:
            sum_result.append(1)

        sum_result.reverse()
        sum_result_str = map(str, sum_result)
        return "".join(sum_result_str)

    def unit_sum(self, num1, num2, carry):
        """
        Binary Sum rule reference
        0 + 0 = 0
        0 + 1 = 1
        1 + 0 = 1
        1 + 1 = 0 (1 gets carry forward)
        1 + 1 + 1 = 1 (1 gets carry forwarded)
        """

        result = carry + num1 + num2

        # Condition to limit to handle addition of 1 + 1
        next_carry = 0
        if result > 1:
            if result == 2:
                result = 0
            elif result == 3:
                result = 1
            next_carry = 1

        return (result, next_carry)


def main():
    a = input("Enter a: ").strip()
    b = input("Enter b: ").strip()

    soln = Solution()
    print(soln.addBinary(a, b))


if __name__ == "__main__":
    main()
