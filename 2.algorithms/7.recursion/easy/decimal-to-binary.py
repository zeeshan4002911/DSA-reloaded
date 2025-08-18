"""
Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent binary number.

Examples :

    Input: d = 7
    Output: 111
    Explanation:  20 + 21  + 22 = 1+2+4 = 7.

    Input: d = 10
    Output: 1010
    Explanation: 21  + 23 = 2+8 = 10.
"""


class Solution:
    def decimal_to_binary_number(self, n):
        binary_str = self.decimal_to_binary_rec_helper(n, "")
        # Reverse and conversion to integer
        return int(binary_str[::-1])

    def decimal_to_binary_rec_helper(self, n, result):
        if n == 1:
            # Additon of 1 as final dividend to result
            return result + "1"

        # Storing remainder of divison by 2 into result
        result += str(n % 2)
        # Floor divison by 2 for reducing the input for next divison
        n //= 2
        return self.decimal_to_binary_rec_helper(n, result)


def main():
    while True:
        n = input("Enter a number: ").strip()
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid", int.__name__)

    solution = Solution()
    print(solution.decimal_to_binary_number(n))


if __name__ == "__main__":
    main()
