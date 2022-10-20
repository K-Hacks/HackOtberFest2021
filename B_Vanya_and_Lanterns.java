// import java.util.Scanner;
import java.util.*;
public class B_Vanya_and_Lanterns{

public static boolean check(double arr[],double gap){
      
     for(int i=1;i<arr.length;i++){
            if(arr[i]-arr[i-1]<=(2*gap)){
                continue;
            }else{
                return false;
            }
    }
   
    return true;

}

 
public static void main(String[] args) {
  
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int l=sc.nextInt();
    double arr[]=new double[n];
    // arr[0]=0,arr[arr.length-1]=l;
    for(int i=0;i<arr.length;i++){
        arr[i]=sc.nextDouble();
    }
        
    //    double start=0,end=l;
    //    double ans=l;
    //    while(start<=end){
    //        double mid=(start+end)/2;
    //        if(check(arr,mid)){
    //            ans=mid;
    //            end=mid-0.000000001;
    //        }else{
    //            start=mid+0.000000001;
    //        }


    //    }

    Arrays.sort(arr);
    double ans=0;
    for(int i=1;i<arr.length;i++){
          double d=arr[i]-arr[i-1];
          d=d/2;
        //   System.out.println(d);
          if(d>ans) ans=d;
           
    }


    double one=arr[0];
    if(one>ans) ans=one;
    double two=l-arr[arr.length-1];
    if(two>ans) ans=two;
    System.out.println(ans);
  


}




}