/**
Example:

Input: ‘N’ = 3

Output: 
1
1 2 
1 2 3

*/

#include<iostream>

int main() {
    int n;
    std::cout << "Enter N for pattern : ";
    std::cin >> n; 

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j < i + 1; j++) {
            std::cout << j << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}