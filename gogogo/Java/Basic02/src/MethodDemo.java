import java.util.Scanner;

public class MethodDemo{
    public static void main(String[] arugs)
    {
       System.out.println(sum(1,2));
       sayHi("����");
       System.out.println(getNum());
    } 
        // 1.�в����з���ֵ
        public static int sum(int a ,int b)
        {
            return a+b;
        }
        // 2.�в����޷���ֵ
        public static void sayHi(String name)
        {
            System.out.println("��Һã��ҽ�"+name);
        }
        //3.�޲����з���ֵ
        public static double getNum()
        {
            return 3.14;
        }
    
              
}