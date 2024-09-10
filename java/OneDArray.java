/*

Take N integers as an input and store them in an array and then print the array in reverse format.



Problem Constraints

1 <= N <= 105

1 <= Array Elements <= 109



Input Format

First line contains a single integer N

Next N lines each contains a single integer denoting the array elements.



Output Format

Output N lines denoting the reverse of the inputted array.



Example Input

Input 1:

 5
 2
 1
 11
 13
 14
Input 2:

 2
 12
 11


Example Output

Output 1:

 14
 13
 11
 1
 2
Output 2:

 11
 12

*/


import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        Scanner sc = new Scanner(System.in);
	System.out.println("Enter the size of array and then following numbers of integers");
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        
        for (int i = n - 1; i >= 0; i--) {
            System.out.println(arr[i]);
        }
    }
}
