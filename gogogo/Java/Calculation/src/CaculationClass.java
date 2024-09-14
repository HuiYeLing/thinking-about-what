import java.util.InputMismatchException;
import java.util.Scanner;

public class CaculationClass {
    public static void main(String[] args) throws Exception {
       int a=0 ,b=0;
       Scanner sc = new Scanner(System.in);
       System.out.println("请输入两个整数：");
        try{
            a=sc.nextInt();
            b=sc.nextInt();
        }
        catch(InputMismatchException e){//捕获输入不是整数的异常
            e.printStackTrace();//打印异常信息
        }
            System.out.println(a+"+"+b+"="+(a+b));
            System.out.println(a+"-"+b+"="+(a-b));
            System.out.println(a+"*"+b+"="+(a*b));
            System.out.println(a+"/"+b+"="+(a/b));
        try{
            System.out.println(a+"/"+b+"="+(a/b));
        }
        catch(ArithmeticException e){//捕获除数为0的异常
            e.printStackTrace();//打印异常信息
        }
    }
}
