/*
Input Format: N = 3
Result: 
* 
* * 
* * *

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *
*/

#include<iostream>

int main() {
    int n;
    std::cout << "Enter N for pattern : ";
    std::cin >> n; 

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            std::cout << "* ";
        }
        std::cout << std::endl;
    }
    return 0;
}