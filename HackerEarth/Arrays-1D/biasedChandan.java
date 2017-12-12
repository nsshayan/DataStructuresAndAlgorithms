/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;
*/
import java.io.BufferedReader;
import java.util.*;

class TestClass {
    public static void main(String args[] ) throws Exception {
        /*
         * Read input from stdin and provide input before running
         * Use either of these methods for input

        //BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);

        //Scanner
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();

        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }
        */
        Stack nos = new Stack();
        int v;
        
        nos.push(0);

        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        
        for (int i=0;i<N;i++){
            v = s.nextInt();
            if (v == 0)
            nos.pop();
            else
            nos.push(v);
        }
        
            

        System.out.println("Hello World!");
    }
}
