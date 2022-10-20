import java.util.*;
import java.lang.*;

public class B_Sort_the_Array
{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int n=sc.nextInt();
      
     int arr[]=new int[n];
     int temp[]=new int[n];

    for(int i=0;i<arr.length;i++){
        arr[i]=temp[i]=sc.nextInt();
    }


    HashMap<Integer,Integer> map=new HashMap<>();
    Arrays.sort(temp);
    for(int i=0;i<temp.length;i++){
        map.put(temp[i],i);
    }

    boolean flag=true;
   int start=-1,end=-1;
   for(int i=0;i<arr.length;i++){
       int idx=map.get(arr[i]);
       if(i+1<n && arr[i+1]>=arr[i]){
             if(idx+1<n && arr[idx+1]!=arr[i+1]){
                System.out.println("no");
                flag=false;
                break;
             }
       }else{
            
              if(start==-1) start=i+1;

                end=i+1;
              
               if(idx-1>=0 && arr[idx-1]!=arr[i+1]){
                System.out.println("no");
                flag=false;
                break;
               }




       }
   }


   if(flag){
       System.out.println("yes");
    if(start!=-1 && end!=-1)
       System.out.println(start+" "+end);
    else
      System.out.println(1+" "+1);

}

}
}