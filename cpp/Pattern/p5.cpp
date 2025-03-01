/*
Example:

Input: ‘N’ = 3

Output: 
* * *
* *
*

*/

#include<iostream>

int main() {
    int n;
    std::cout << "Enter N for pattern : ";
    std::cin >> n; 

    for (int i = n; i > 0; i--) {
        for (int j = i; j > 0; j--) {
            std::cout << "* ";
        }
        std::cout << std::endl;
    }
    return 0;
}