import java.util.*;
import java.lang.*;
import java.math.BigInteger;

public class A_PizzaForces{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
        long n=sc.nextLong();
        //minimum time take will be 15 
        System.out.println(Math.max(15,(n+1)/2*5));
         
     }
}
}