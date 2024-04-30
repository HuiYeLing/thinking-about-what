import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        //完成注册系统
        //要求ID为邮箱，密码必须包含数字和字母

        Scanner scan=new Scanner(System.in);
        //获取邮箱
        String mailregex = "^[a-z]\\w{4,12}@\\w+(\\.\\w+)+";
        //获取密码
        String pwdregex="\\w{4,15}";
        boolean mailflag=true;
        while (mailflag) {
            System.out.println("请输入邮箱：");
            String mail=scan.next().trim();
            if(mail.matches(mailregex))
            {
                mailflag=false;
            }
            else
            {
                System.out.println("邮箱不合法，结束程序");
                break;
            }
        }
        boolean pwdflag=true;
        while (pwdflag) {
            System.out.println("请输入密码（4-15位的数字）：");
            String pwd=scan.next().trim();
            if(pwd.matches(pwdregex))
            {
                System.out.println("请再次输入密码：");
                String pwd2=scan.next().trim();
                if(pwd.equals(pwd2))
                {
                    System.out.println("注册成功");
                    pwdflag=false;
                }
                else
                {
                    System.out.println("两次密码不一致，结束程序");
                    break;
                }
                
            }
            else
            {
                System.out.println("密码不合法，结束程序");
                break;
            }
        }
    }
}
