/*

You need to answer Q queries, in each query you are given two integers x and y:

if x = 1 then push the integer y  to the back of the queue.
if x = 2 then return the front element of the queue if the queue is not empty else return -1
if x = 3  then remove the front element from the queue if the queue is not empty else do nothing. No need to return anything in this query.

Problem Constraints

1 <= Q <= 100

1 <= x <= 3

1 <= y <= 100


Input Format

First line of input contains a single integer Q.

Next Q lines each contain two integers x and y for that query.


Output Format

For each query in which x = 2 print its answer in separate lines.


Example Input

Input 1:

 5
 2 -1
 1 5
 3 -1
 1 5
 2 -1

Example Output

Output 1:

 -1
 5

Example Explanation

Explanation 1:

 Query 1: x = 2 so we need to print the front element of the queue , since the queue is empty we will print -1.
 Query 5: x = 2 Queue contains only element 5 so we will print 5.

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
        Queue<Integer> questions = new ArrayDeque<Integer>();
        
        int totalQuestion = sc.nextInt();
        while(totalQuestion != 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            switch(x) {
                case 1:
                    questions.add(y);
                    break;
                case 2:
                    Integer head = questions.peek();
                    if (head != null) {
                        System.out.println(head);
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 3:
                    if (questions.peek() != null) {
                        questions.remove();
                    }
            }
            totalQuestion--;
        }
    }
}
