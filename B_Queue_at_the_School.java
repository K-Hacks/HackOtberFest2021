
import java.util.*;
import java.lang.*;

public class B_Queue_at_the_School
{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int n=sc.nextInt();
     int t=sc.nextInt();
     String s=sc.next();
     char arr[]=s.toCharArray();
     for(int i=0;i<t;i++){
         int j=0;
         while(j<n){
             if(j+1<n && arr[j]=='B' && arr[j+1]=='G'){
                arr[j]='G';
                arr[j+1]='B';
                j=j+2;
             }else{
                 ++j;
             }
         }
     }

     for(char c:arr){
         System.out.print(c);
     }

}
}