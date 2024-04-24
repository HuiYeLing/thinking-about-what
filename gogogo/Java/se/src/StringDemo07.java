import java.util.Scanner;

public class StringDemo07 {
    public static void main(String[] args) {
        //TODO Auto-generated method stub
        //
        //完成注册系统
        //要求ID为邮箱，密码必须包含数字和字母
        //

        Scanner scan=new Scanner(System.in);
        //获取邮箱
        String mailregex="\\w+@\\w+(\\.\\w+)+";
        //获取密码
        
        String pwdregex="[A-Z]+\\w+";
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
                System.out.println("邮箱不合法，请重新输入");
            }
        }
        boolean pwdflag=true;
        while (pwdflag) {
            System.out.println("请输入密码（请输入一位大写字母和任意数量的数字或者字母）：");
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
                    System.out.println("两次密码不一致，请重新输入");
                }
                
            }
            else
            {
                System.out.println("密码不合法，请重新输入");
            }
        }
    }
}
