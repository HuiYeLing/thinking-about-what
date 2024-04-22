import java.util.Scanner;
public class UPDemo {
    public static void main(String[] args) {
        UnionPay up1=new ICBCImpl();
        //
        Scanner scan=new Scanner(System.in);
        System.out.println("请输入密码：");
        //旧写法 String input=scan.next();
        if (up1.checkPwd(scan.next())) 
        {
             System.out.println("密码正确");
             double mon=scan.nextDouble();
             if (up1.drawMoney(mon)) {
                 System.out.println("取款成功，余额："+up1.getMoney());
             }
             else {
                 System.out.println("取款失败，余额不足");
                
             }
        }
        else 
        {
            System.out.println("密码错误");
        }
    }
}
