import java.util.*;
import java.lang.*;

public class B_Moamen_and_k_subarrays{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int t=sc.nextInt();
    while(t-->0){
        int n=sc.nextInt(),k=sc.nextInt();
        int arr[]=new int[n];
        int s[]=new int[n];
        for(int i=0;i<arr.length;i++){
              arr[i]=s[i]=sc.nextInt();
        }
       

        Arrays.sort(s);
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<s.length;i++){
            map.put(s[i],i);
        }

         int teams=1;
         for(int i=1;i<arr.length;i++){
              if(arr[i]>arr[i-1]){
                  int it=map.get(arr[i]);
                  if(it-1>=0 && s[it-1]==arr[i-1]){
                           continue;
                  }else{
                      ++teams;
                  }
              }else{
                  ++teams;
              }
         }

 

         if(teams>k){
             System.out.println("No");
         }else{
             System.out.println("Yes");
         }


    }


}
}