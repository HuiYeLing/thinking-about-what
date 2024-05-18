import java.util.Scanner;

public class eaxm02 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int number=scan.nextInt();
        int numb1,numb2;
        System.out.println("请输入一个整数：");

        System.out.println("数" + number + "的乘法表为：");
        for(numb1=0,numb2=number;numb1<=number;numb1++,numb2--){
            System.out.println(numb1 + " * " + numb2 + " = " + numb1*numb2);
        }
    }
}
