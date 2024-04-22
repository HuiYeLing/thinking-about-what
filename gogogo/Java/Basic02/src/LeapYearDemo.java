import java.util.Scanner;

public class LeapYearDemo {
    public static void main(String[] args) {
        System.out.println("请输入一个年份");
        Scanner in=new Scanner(System.in);//输入工具人
        int year=in.nextInt();//保存输入的年份
        boolean isLeapYear=((year%4==0&&year%100!=0)||(year%400==0))?true:false;
        String str=isLeapYear?year+"是闰年":year+"不是闰年";
        System.out.println(str);
    }
}
