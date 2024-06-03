import java.util.Scanner;

public class string11 {
    public static void main(String[] args) {
        String str = "中国首都是北京，北京很大！";
        String subStr ;
        int count = 0;
        int index = 0;
        System.out.println("请输入要查找的字符串");
        Scanner scan = new Scanner(System.in);
        subStr = scan.next();
        while ((index = str.indexOf(subStr, index)) != -1) {
            count++;
            index += subStr.length();
        }

        System.out.println(subStr + "在 中国首都是北京，北京很大！ 出现的次数为: " + count);
    }
}