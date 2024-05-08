/*
Data type refers to the type of value a variable has and the way the computer interprets it.

Each data type has a different size. You’ve studied 5 different data types and the sizes of the data types:

Integer: 4 bytes
Long: 8 bytes
Float: 4 bytes
Double: 8 bytes
Character: 1 byte


You’re given a data type. Print its size in bytes.


Example :

Input: Long

Output: 8

Explanation: The size of a Long variable is given as 8 bytes.

*/

#include<iostream>
#include<string>

int dataTypes(std::string type) {
    if(type=="Long"){
        return 8;
    }
    else if(type=="Integer"){
        return 4;
    }
    else if(type=="Float"){
        return 4;
    }
    else if(type=="Double"){
        return 8;
    }
    else if(type=="Character"){
        return 1;
    } else {
        return 0;
    }
}

int main() {
    std::string dataType;
    std::cout << "Enter a data type (e.g., Integer, Float, Double, Character): ";
    std::getline(std::cin, dataType);
    
    std::cout << "Result is: " << dataTypes(dataType);
    return 0;
}