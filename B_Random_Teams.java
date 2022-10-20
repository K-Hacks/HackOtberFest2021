import java.util.*;
import java.lang.*;

public class B_Random_Teams{

public static long pair(long n){
    return n*(n-1)/2;
}
public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    // int t=sc.nextInt();
    // while(t-->0){
        int n=sc.nextInt();
        int m=sc.nextInt();

        //max
        long left=n-m+1;
        long max=((left-1)*left)/2; 

        //min
        long mod=n%m;
        long item=n/m;
        long onep=m-mod;
        long twop=mod;
        long min=(onep*pair(item))+(twop*pair(item+1));
       
           System.out.println(min+" "+max);

    // }

}

}
