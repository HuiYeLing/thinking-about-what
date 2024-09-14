
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        double a,b,c;
        Scanner in = new Scanner(System.in);
        System.out.println("请输入三角形的三边：");
        a=in.nextDouble();
        b=in.nextDouble();
        c=in.nextDouble();
        Triangle t = new Triangle(a,b,c);
        try {
            t.judgeTriangle();
        } catch (EdgeException e) {
            e.printStackTrace();
        }
}
}







