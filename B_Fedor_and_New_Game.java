import java.util.*;
import java.lang.*;

public class B_Fedor_and_New_Game{

    public static int solve(int A, int B,int n){
        int count = 0;
        // int temp=A^B;
        for(int i=0;i<n;i++){
            int one=A|0;
            int two=B|0;
            if(one!=two) ++count;

        }
        return count;
    }


public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int n=sc.nextInt();
     int m=sc.nextInt();
     int k=sc.nextInt();

    
     int arr[]=new int[m+1];
     for(int i=0;i<arr.length;i++){
         arr[i]=sc.nextInt();
     }

  
     int friends=0;
     for(int i=arr.length-2;i>=0;i--){
         int temp=solve(arr[arr.length-1],arr[i],n);
         if(temp<=k) ++friends;
     }

     System.out.println(friends);
    

    
}
}