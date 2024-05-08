/*

The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -

    F(n) = F(n - 1) + F(n - 2),
    Where, F(1) = 1, F(2) = 1


Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.

"Indexing is start from 1"


Example :

Input: 6

Output: 8

Explanation: The number is ‘6’ so we have to find the “6th” Fibonacci number.
So by using the given formula of the Fibonacci series, we get the series:
[ 1, 1, 2, 3, 5, 8, 13, 21]
So the “6th” element is “8” hence we get the output.

*/

#include <bits/stdc++.h>

int main() {
    int n;
    std::cout << "Enter nth number (n) : ";
    std::cin >> n;
    int prev, prev_prev = 1;
    int current;
    for (int i = 0; i < n; i++) {
        current = prev + prev_prev;
        std::cout << current << " ";
        prev_prev = prev;
        prev = current;
    }
    std::cout << "\n" << "Element is : " << current;
    return 0;
}