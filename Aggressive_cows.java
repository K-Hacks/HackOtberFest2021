// t – the number of test cases, then t test cases follows.
// * Line 1: Two space-separated integers: N and C
// * Lines 2..N+1: Line i+1 contains an integer stall location, xi

import java.util.*;
import java.lang.*;
// Aggressive_cows
public class Aggressive_cows{

public static boolean check(int arr[],int gap,int cows){
   int count=1;
   int last=arr[0];
  for(int i=1;i<arr.length;i++){

           if(arr[i]-last>=gap){
               ++count;
               last=arr[i];
           }
  }

   if(count>=cows) return true;
   
   return false;

}

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
         int n=sc.nextInt();
         int c=sc.nextInt();
         int arr[]=new int[n];
         for(int i=0;i<arr.length;i++){
             arr[i]=sc.nextInt();
         }
         
         Arrays.sort(arr);
        //  for(int i:arr)
        //  System.out.print(i+" ");
                  
         int low=0,high=arr[arr.length-1]-arr[0];
         int ans=0;
         while(low<=high){
             int mid=(low+high)/2;
             if(check(arr,mid,c)){
                 low=mid+1;
                 ans=Math.max(ans,mid);
             }else{
                  high=mid-1;
             }

         }

// System.out.println(check(arr,3,3));

   
         System.out.println(ans);


     }
}
}