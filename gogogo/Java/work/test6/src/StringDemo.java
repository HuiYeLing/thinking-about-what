
import java.util.Scanner;
import java.util.regex.Pattern;

public class StringDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("请输入用户名：");
        String username = scanner.nextLine();
        String usernameRegex = "^[a-z]\\w{4,9}@\\w+\\.com$";
        if (!Pattern.matches(usernameRegex, username)) {
            System.out.println("用户名不可以使用");
            scanner.close();
            return;
        }

        System.out.println("请输入密码：");
        String password = scanner.nextLine();
        String passwordRegex = "^[a-zA-Z]{4,10}$";
        if (!Pattern.matches(passwordRegex, password)) {
            System.out.println("不可以使用");
        } else {
            System.out.println("可以使用");
        }

        scanner.close();
    }
}

