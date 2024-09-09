/*
Example:

Input: ‘N’ = 3

Output: 

*
**
***
**
*


*/

#include<iostream>

int main() {
    int n;
    std::cout << "Enter N for pattern : ";
    std::cin >> n; 

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
    for (int i = n - 1; i > 0; i--) {
        for (int j = 1; j <= i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    // With Two for loops only
    // for(int i = 1; i <= 2 * n - 1; i++){          
    //     int stars = i;
    //     if(i > n) stars = 2 * n - i;
    //     for(int j = 1; j <= stars; j++){
    //         std::cout << "*";
    //     }
    //     std::cout << std::endl;
    // }

    return 0;
}