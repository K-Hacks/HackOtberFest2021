import java.util.*;
import java.lang.*;

public class B_Combinatorics_Homework{

public static void main(String[] args){
    Scanner s=new Scanner(System.in);
     int t=s.nextInt();
     while(t-->0){
      
			int[] a = new int[3];
 
			a[0] = s.nextInt();
			a[1] = s.nextInt();
			a[2] = s.nextInt();
			int m = s.nextInt();
			Arrays.sort(a);
 
			int max = a[0] - 1 + a[1] - 1 + a[2] - 1;
			int min = a[2] - a[1] - a[0] - 1;
 
			System.out.println(m >= min && m <= max?"YES":"NO");



     }
}
}