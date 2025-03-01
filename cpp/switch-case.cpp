/*
Programming languages have some conditional / decision-making statements that execute when some specific condition is fulfilled.


Switch-case is one of the ways to implement them.


In a menu-driven program, the user is given a set of choices of things to do (the menu) and then is asked to select a menu item.


There are 2 choices in the menu:


Choice 1 is to find the area of a circle having radius 'r'.

Choice 2 is to find the area of a rectangle having dimensions 'l' and 'b'.


You are given the choice 'ch' and an array 'a'.


If ‘ch’ is 1, ‘a’ contains a single number ‘r’. If ‘ch’ is 2, ‘a’ contains 2 numbers, ‘l’ and ‘b’.


Consider the choice and print the appropriate area.


Example :

Input: ‘ch’ = 2 and ‘a’ = [3, 2]

Output: area = 6

Explanation: Since the choice ‘ch’ is 2, we have to print the area of the rectangle having ‘l’ = 3 and ‘b’ = 2, which is 6.

*/

#include <iostream>
#include <math.h>
#include <vector>

double areaSwitchCase(int ch, std::vector<double> a) {
    double area; 
    switch(ch) {
        case 1:
            area = M_PI * pow(a[0], 2);
            break;
        case 2:
            area = a[0] * a[1];
    }
    return area;
}

int main() {
    int choice;
    std::cout << "Enter choice for aread calculation (circle - 1, rectangel - 2) : ";
    std::cin >> choice;
    std::vector<double> inputs;
    double num;
    for (int i = 0; i < choice; i++) {
        std::cout << "Enter number : ";
        std::cin >> num;
        inputs.push_back(num);
    }
    double result = areaSwitchCase(choice, inputs);
    std::cout << "Calculated Area : " << result;
    return 0;
}