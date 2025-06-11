"""
Fizz Buzz Problem involves that given an integer n, for every integer 0 < i <= n, the task is to output,

    "FizzBuzz" if i is divisible by 3 and 5,
    "Fizz" if i is divisible by 3,
    "Buzz" if i is divisible by 5
    "i" as a string, if none of the conditions are true.

Return an array of strings.

Examples :

Input: n = 3
Output: ["1", "2", "Fizz"]
Explanation: 1 and 2 are neither divisible by 3 nor 5, so we just output 1 and 2, and 3 is divisible by 3 so we output "Fizz".

Input: n = 10
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]

Input: n = 20
Output: [“1”, “2”, “Fizz”, “4”, “Buzz”, “Fizz”, “7”, “8”, “Fizz”, “Buzz”, “11”, “Fizz”, “13”, “14”, “FizzBuzz”, “16”, “17”, “Fizz”, “19”, “Buzz”]

Constraints:
1 ≤ n ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def fizz_buzz_hashing(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            hash_value = self.hash_helper(i)
            result.append(hash_value)
        return result

    def hash_helper(self, n):
        hash_value = ""
        hash_map = {"3": "Fizz", "5": "Buzz"}
        divisors_order = [3, 5]
        
        # Hashing the value based on hash modulo condition
        for d in divisors_order:
            if n % d == 0:
                hash_value += hash_map[str(d)]

        if hash_value == "":
            hash_value = str(n)
        return hash_value


def main():
    n = int(input())
    solution = Solution()
    print(solution.fizz_buzz_hashing(n))


if __name__ == "__main__":
    main()
