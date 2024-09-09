/*
Example:

Input: ‘N’ = 3

Output: 

  *
 ***
*****
*****
 ***
  *

*/

#include<iostream>

int main() {
    int n;
    std::cout << "Enter N for pattern : ";
    std::cin >> n; 

    // Erected Pyramid
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            std::cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    // Inverted Pyramid 
    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j < n - i - 1; j++) {
            std::cout << " ";
        }
        for (int j = 0; j < 2 * i + 1; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    return 0;
}