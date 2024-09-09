/**
Input: ‘N’ = 3

Output: 

1 2 3
1 2
1 
*/

#include<iostream>

int main() {
    int n;
    std::cout << "Enter N for pattern : ";
    std::cin >> n; 

    for (int i = n; i > 0; i--) {
        for (int j = 1; j <= i; j++) {
            std::cout << j << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
