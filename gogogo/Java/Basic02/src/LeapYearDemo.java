import java.util.Scanner;

public class LeapYearDemo {
    public static void main(String[] args) {
        System.out.println("������һ�����");
        Scanner in=new Scanner(System.in);//���빤����
        int year=in.nextInt();//������������
        boolean isLeapYear=((year%4==0&&year%100!=0)||(year%400==0))?true:false;
        String str=isLeapYear?year+"������":year+"��������";
        System.out.println(str);
    }
}
