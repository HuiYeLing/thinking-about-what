import java.util.Scanner;
public class MethodDemo03 {
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        int a=scan.nextInt();
        int b=scan.nextInt();
        int c=scan.nextInt();
        System.out.println(max(max(a,b),c));
    }
    public static int max(int x,int y)
    {
        if (x>y)return x;
        return y;
    }
}
