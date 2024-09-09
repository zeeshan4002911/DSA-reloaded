/*

Given an integer n as an input print the numbers from 1 to n in separate lines.

Problem Constraints

1 <= n <= 100


Input Format

A single line of input containing an integer n.


Output Format

Print all the numbers from 1 to n in separate lines.


Example Input

Input 1:

 5
Example Output

Output 1:

 1
 2
 3
 4
 5

*/


import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        /***Don't change the code here***/
        Scanner inp = new Scanner(System.in);
	System.out.print("Enter the value of N: ");
        int n = inp.nextInt();
        inp.close();
        /***********************************/
        
        
        /***Your code goes here***/
        
        for (int i = 1; i <= n; i++) {
            System.out.println(i);
        }
    }
}
