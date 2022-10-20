import java.util.*;
import java.lang.*;

public class B_Two_Tables{

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
         int W=sc.nextInt(),H=sc.nextInt();
         int x1=sc.nextInt(),y1=sc.nextInt(),x2=sc.nextInt(),y2=sc.nextInt();
         int w2=sc.nextInt(),h2=sc.nextInt();
         int w1=(x2-x1),h1=(y2-y1);

         int min=Integer.MAX_VALUE; 
        boolean flag=true; 
        if(w1+w2>W && h1+h2>H){
            System.out.println(-1);
            // min=-1;
            flag=false;
        } 

       
        if(flag && w1+w2<=W){
          int index1=w2,index2=W-w2;
          if(index1>x1){
              min=Math.min(min,index1-x1);
          }else{
              min=0;
          }

           
          if(index2<x2){
            min=Math.min(min,x2-index2);
        }else{
            min=0;
        }

        }

        if(flag && h1+h2<=H){
            int index1=h2,index2=H-h2;
            if(index1>y1){
                min=Math.min(min,index1-y1);
            }else{
                min=0;
            }

            if(index2<y2){
                min=Math.min(min,y2-index2);
            }else{
                min=0;
            }

        }

   if(flag){
  double ans=(1.000000000)*min;
  System.out.println(ans);
    }

     }
}
}