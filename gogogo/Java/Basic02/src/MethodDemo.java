import java.util.Scanner;

public class MethodDemo{
    public static void main(String[] arugs)
    {
       System.out.println(sum(1,2));
       sayHi("张三");
       System.out.println(getNum());
    } 
        // 1.有参数有返回值
        public static int sum(int a ,int b)
        {
            return a+b;
        }
        // 2.有参数无返回值
        public static void sayHi(String name)
        {
            System.out.println("大家好，我叫"+name);
        }
        //3.无参数有返回值
        public static double getNum()
        {
            return 3.14;
        }
    
              
}