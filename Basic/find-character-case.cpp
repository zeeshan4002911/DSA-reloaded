/*
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.


1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.


Example:

Input: The character is 'a'.

Output: 0

Explanation: The input character is lowercase, so our answer is 0.

*/


#include<iostream>

int find_character_case() {
	char input;
	std::cin >> input;
	int input_ascii = int(input);
	if (input_ascii >= 65  && input_ascii <= 90) {
		return 1;
	} else if (input_ascii >= 97 && input_ascii <= 122) {
		return 0;
	}
	return -1;
}

int main() {
	std::cout << "Enter a character: ";
    int result = find_character_case();
    std::cout << "The result is " << result;
    return 0;
}
