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