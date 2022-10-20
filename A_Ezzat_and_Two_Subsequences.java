import java.util.*;
import java.lang.*;

public class A_Ezzat_and_Two_Subsequences{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
         int n=sc.nextInt();
         int arr[]=new int[n];
         for(int i=0;i<arr.length;i++){
             arr[i]=sc.nextInt();
         }

        Arrays.sort(arr);
        double temp=arr[arr.length-1];
        double sum=0;
        for(int i=0;i<arr.length-1;i++){
          sum+=arr[i];
        }
   
        double avg=(sum*1.0)/(arr.length-1);
        System.out.println(avg+temp);
       

     }
}
}