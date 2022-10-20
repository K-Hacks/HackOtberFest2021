import java.util.*;
import java.lang.*;

public class A_Mocha_and_Math{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
         int n=sc.nextInt();
         int ans=sc.nextInt();
         for(int i=1;i<n;i++){
             ans=ans&(sc.nextInt());
         }
    
        System.out.println(ans);

        //  int min=Integer.MAX_VALUE;
        //  for(int i=0;i<arr.length;i++){
        //      for(int j=i;j<arr.length;j++){
        //          int l=i,r=j;
        //          int max=Integer.MIN_VALUE;
        //         for(int k=0;k<=r-l;k++){
        //            int temp=arr[l+k]&arr[r-k];
        //            max=Math.max(max,temp);
        //         }
        //         min=Math.min(min,max);
        //      }
        //  }
        


     }
}
}