import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    int[][] x = {{4,5,6},{3,4,5},{1,6,7}};
	    int[][] y = {{5,7,9},{5,3,2},{10,1,5}};
	    int[][] z =new int[3][3];
	    for(int a=0;a<3;a++){
	        for(int b=0;b<3;b++){
	            z[a][b]=0;
	            for(int c=0;c<3;c++){
	                z[a][b]=z[a][b] + x[a][c] * y[c][b];
	                
	            }
	            System.out.print(z[a][b]+" ");
	        }
	        System.out.println(" ");
	    }
	
	}
}
