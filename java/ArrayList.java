/*

You are given a stream of positive integers as input and the stream ends when you encounter an negative element.

You need to save this numbers in an ArrayList and then print this numbers in reverse order.

NOTE: See example input/output for further understanding



Input Format

Input contains of several lines where each line contain a single integer denoting the stream of integers.


Output Format

Output the inputted stream in reverse format as space-separated integers in a single line.


Example Input

Input 1:

 11
 1
 2
 6
 0
 -2
Input 2:

 10
 2
 -1
Example Output

Explanation 1:

 0 6 2 1 11
Explanation 2:

 2 10
Example Explanation

Explanation 1:

 The inputted stream looks like: [11, 1, 2, 6, 0]
 We need to print the reverse of this.

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
        ArrayList arrayList = new ArrayList<>();
        int currentVal = sc.nextInt();
        while(currentVal >= 0) {
            arrayList.add(currentVal);
            currentVal = sc.nextInt();
        }
        sc.close();
        int n = arrayList.size();
        for (int i = n - 1; i >= 0; i--) {
            System.out.print(arrayList.get(i) + " ");
        }
	System.out.println();
    }
}
