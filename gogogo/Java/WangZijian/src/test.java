import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        // 完成注册系统
        // 要求ID为邮箱，密码必须包含数字和字母

        Scanner scan = new Scanner(System.in);
        // 定义邮箱的正则表达式，要求以小写字母开头，后面跟4到12个字符，然后是@符号，之后是域名
        String mailregex = "^[a-z]\\w{4,12}@\\w+(\\.\\w+)+";
        // 定义密码的正则表达式，要求是4到15位的任意字符（这里的正则表达式并没有严格限制必须包含数字和字母）
        String pwdregex = "\\w{4,15}";
        boolean mailflag = true;
        while (mailflag) {
            System.out.println("请输入邮箱：");
            String mail = scan.next().trim(); // 获取用户输入的邮箱，并去除前后空格
            if (mail.matches(mailregex)) {
                mailflag = false; // 如果邮箱匹配正则表达式，则结束循环
            } else {
                System.out.println("邮箱不合法，结束程序");
                break; // 如果邮箱不合法，则结束程序
            }
        }
        boolean pwdflag = true;
        while (pwdflag) {
            System.out.println("请输入密码（4-15位的数字）："); // 这里的提示信息有误，应为“4-15位的字符”
            String pwd = scan.next().trim(); // 获取用户输入的密码，并去除前后空格
            if (pwd.matches(pwdregex)) {
                System.out.println("请再次输入密码：");
                String pwd2 = scan.next().trim(); // 获取用户再次输入的密码，并去除前后空格
                if (pwd.equals(pwd2)) {
                    System.out.println("注册成功");
                    pwdflag = false; // 如果两次密码一致，则注册成功，结束循环
                } else {
                    System.out.println("两次密码不一致，结束程序");
                    break; // 如果两次密码不一致，则结束程序
                }

            } else {
                System.out.println("密码不合法，结束程序");
                break; // 如果密码不匹配正则表达式，则结束程序
            }
        }
    }
}