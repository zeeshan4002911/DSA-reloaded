/*

Take 2D matrix A of size N X M as an input and print M integers denoting the column-wise sum of each of the M columns.


Problem Constraints

1 <= N, M <= 103

1 <= A[i][j] <= 100


Input Format

First line contains two space-separated integers N and M.

Each of the next N lines contains M space-separated integers denoting the matrix elements.


Output Format

Print M space-separated integers where each denoting the column-wisw sum of A.


Example Input

Input 1:

 3 4
 3 2 1 3
 1 2 3 4
 4 3 1 2

Example Output

Output 1:

 8 7 5 9

Example Explanation

Explanation 1:

 Sum of elements of first column : 3 + 1 + 4 = 8
 Sum of elements of second column : 2 + 2 + 3 = 7
 Sum of elements of third column : 1 + 3 + 1 = 5
 Sum of elements of fourth column : 3 + 4 + 2 = 9

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
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] matrix = new int[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        sc.close();
        for (int i = 0; i < m; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += matrix[j][i];
            }
            System.out.print(sum + " ");
        }
        System.out.println();
    }
}
