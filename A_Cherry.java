import java.util.*;
import java.lang.*;
import java.math.BigInteger;

public class A_Cherry{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
        //  long mod=1000
         int n=sc.nextInt();
         int arr[]=new int[n];
         for(int i=0;i<arr.length;i++){
             arr[i]=sc.nextInt();
         }

       boolean flag=true;
       for(int i=1;i<arr.length;i++){
           if(arr[i]!=arr[i-1]){
               flag=false;
               break;
           }
       }

  
       if(!flag){
         int one=Integer.MIN_VALUE;
         for(int i:arr){
             one=Math.max(one,i);
         }
         
         int two=Integer.MIN_VALUE;
         for(int i=0;i<arr.length;i++){
             if(two<arr[i] && arr[i]!=one){
                 two=arr[i];
             }
         }
         
         BigInteger a=BigInteger.valueOf(one);
         BigInteger b=BigInteger.valueOf(two);
         BigInteger ans=a.multiply(b);
         System.out.println(ans);  

       }else{
          
        BigInteger a=BigInteger.valueOf(arr[0]);
        BigInteger b=BigInteger.valueOf(arr[0]);
        BigInteger ans=a.multiply(b);
        System.out.println(ans); 
       }

       

     }
}
}