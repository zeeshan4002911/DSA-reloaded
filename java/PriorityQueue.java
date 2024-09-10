/*

You need to think of a data structure and implement it such that it can help you in answering the below-mentioned queries.

You are given Q queries, in each query you are given two integers x and y:

if x = 1 then insert the integer y to your data structure.
if x = 2 then print an integer denoting the minimum element currently present in your data-structure, if there are no elements present then print -1
if x = 3 then remove the minimum element currently present in your data structure, if there is no element present then don't do anything.
 



Problem Constraints

1 <= Q <= 105

1 <= x <= 3

1 <= y <= 1000


Input Format

The first line of input contains a single integer Q.

Next, Q lines each contain two integers x and y for that query.


Output Format

For each query in which x = 2 print its answer in separate lines.


Example Input

Input 1:

 6
 2 -1
 1 5
 1 2
 2 -1
 3 -1
 2 -1

Example Output

Output 1:

 -1
 2
 5

Example Explanation

Explanation 1:

 Query 1: x = 2 but as we don't have any element so we will print -1.
 Query 2: x = 1 we will insert 5 to our data structure.
 Query 3: x = 1 we will insert 2 to our data structure.
 Query 4: x = 2 the minimum element is 2
 Query 5: x = 3 we will remove the minimum element i.e 2
 Query 6: x = 2 the minium element now is 5

*/


import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // YOUR CODE GOES HERE
        // Please take input and print output to standard input/output (stdin/stdout)
        // DO NOT USE ARGUMENTS FOR INPUTS
        // E.g. 'Scanner' for input & 'System.out' for output
        PriorityQueue<Integer> questions = new PriorityQueue<>();
        Scanner sc = new Scanner(System.in);
        
        int totalQuestions = sc.nextInt();
        while(totalQuestions > 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            switch (x) {
                case 1:
                    questions.add(y);
                    break;
                case 2:
                    Integer head = questions.peek();
                    if (head != null)
                        System.out.println(head);
                    else
                        System.out.println(-1);
                    break;
                case 3:
                    if (questions.peek() != null) {
                        questions.remove();
                    }
            }
            totalQuestions--;
        }
    }
}
