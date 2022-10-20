import java.util.*;
import java.lang.*;

public class A_Regular_Bracket_Sequences{

public static Set<String> f(int n){

    if(n==1){
        Set<String> temp=new HashSet<>();
        temp.add("()");
        return temp;
    }

    // (+prev+)
    // ()+prev
    // prev+()


    Set<String> prev=f(n-1);
    Set<String> ans=new HashSet<>();
    for(String item:prev){
           String one="()"+item;
           String two=item+"()";
           String three="("+item+")";
           ans.add(one);
           ans.add(two);
           ans.add(three);
           if(ans.size()==n) return ans;
    }
  

      return ans;
     

}

public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
     int t=sc.nextInt();
     while(t-->0){
         int n=sc.nextInt();
        //  Set<String> set=new HashSet<>();
         int count=0;
         Set<String> set=f(n);
         for(String item:set){
             if(count<(n)){
                 System.out.println(item);
                 ++count;
             }else{
                 break;
             }
             
         }
     }
}
}