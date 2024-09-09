/*
Their exist two lines of input each consist of single integer, read these two integers using BufferedReader Class and then print both of them on a single line in a space-separated manner.


Input Format
Input consist of two lines.

Both of the lines contains a single integer.


Output Format
Print both of the integers on a single line in a space-separated manner.


Example Input
Input 1:

 12
 1
Input 2:

 12
 110


Example Output
Output 1:

 12 1
Output 2:

 12 110

*/

import java.lang.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferReader {
    public static void main(String[] args) throws IOException {
        InputStreamReader inputStreamReaderObj = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(inputStreamReaderObj);
        System.out.println("Input two numbers seperated by newline for reading");
	int num1 = Integer.parseInt(reader.readLine());
        int num2 = Integer.parseInt(reader.readLine());
        System.out.println(num1 + " " + num2);
    }
}
