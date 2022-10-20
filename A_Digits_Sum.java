import java.util.*;
import java.lang.*;

public class A_Digits_Sum{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
         long n=sc.nextLong();
         long ans=(n+1)/10;
         if(n<9)
         ans=0;
         if(n==9)
         ans=1;

         System.out.println(ans);
     }
}
}