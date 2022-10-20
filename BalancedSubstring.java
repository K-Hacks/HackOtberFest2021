import java.util.*;
// BalancedSubstring
public class  BalancedSubstring{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            String str=sc.next();
            boolean flag=false;
            int i1=-1,i2=-1; 

            for(int i=0;i<str.length();i++){
                int a=0;
                int b=0;

                for(int j=i;j<str.length();j++){
                   if(str.charAt(j)=='a'){
                       ++a;
                   }else{
                       ++b;
                   }
                    
                   if(a>0 && b>0 && a==b){
                       i1=i+1;
                       i2=j+1;
                       flag=true;
                   }

                }

                if(flag){
                   break; 
                } 

            }

          
             System.out.println(i1+" "+i2);
         
          

        }
    }
}
