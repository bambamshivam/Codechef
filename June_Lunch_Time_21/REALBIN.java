import java.util.*;
class REALBIN{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			long a=sc.nextInt();
			long b=sc.nextInt();
			while(b%2==0){
				b=b/2;
			}
			if(b==1){
				System.out.println("Yes");
			}
			else{
				System.out.println("No");
			}
		}
	}
}