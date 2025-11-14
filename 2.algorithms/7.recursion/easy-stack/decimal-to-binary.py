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

from queue import LifoQueue


class Solution:
    def decimal_to_binary_number_iterative(self, n):
        st = LifoQueue()

        # Putting initial value to stack
        st.put((n, ""))

        while True:
            # Retriving the last run value
            n, result = st.get()

            # Base case to terminate the iteration
            if n == 1:
                st.put((n, result + "1"))
                break

            # Core logic of conversion
            result += str(n % 2)
            n //= 2
            st.put((n, result))

        final_res = st.get()[1]
        binary_num = int(final_res[::-1])
        return binary_num


def main():
    while True:
        n = input("Enter a number: ").strip()
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid", int.__name__)

    solution = Solution()
    print(solution.decimal_to_binary_number_iterative(n))


if __name__ == "__main__":
    main()
