/*

You are given two integers as input a and b

You need to perform several tasks in the editor below:

In the variable named "add" store the sum of a and b.
In the variable named "sub" store the difference of a with b.
In the variable named "multi" store the multiplication of a and b.
In the variable named "div" store the division of a by b.

*/

import java.lang.*;
import java.util.*;

public class Operators {
    public static void main(String[] args) {
    
    /***Don't change anything here***/
        Scanner inp = new Scanner(System.in);
	System.out.println("Enter two numbers for operation seperated by newline");
        int a = inp.nextInt();
        inp.nextLine();
        int b = inp.nextInt();
        inp.nextLine();
        inp.close();
    /*********************************/
    
    /*Perform the task here*/
        
        int add;
        int sub;
        int multi;
        int div;
        
        add = a + b;
        sub = a - b;
        multi = a * b;
        div = a / b;
        
    /***********************/
    
    /******Don't change anything here******/
        System.out.println(add);
        System.out.println(sub);
        System.out.println(multi);
        System.out.println(div);
    
    }
}
