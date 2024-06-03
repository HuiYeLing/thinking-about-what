import java.util.Scanner;

public class Register {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        StringBuilder errors = new StringBuilder();

        System.out.println("请输入Java工程师用户名：");
        String username = scanner.nextLine();
        if (username.length() < 6) {
            errors.append("用户名长度不能小于6\n");
        }

        System.out.println("请输入密码：");
        String password = scanner.nextLine();
        if (password.length() < 8) {
            errors.append("密码长度不能小于8\n");
        }

        System.out.println("请再次输入密码：");
        String confirmPassword = scanner.nextLine();
        if (!password.equals(confirmPassword)) {
            errors.append("两次输入的密码不一致\n");
        }

        if (errors.length() > 0) {
            System.out.println(errors.toString());
        } else {
            System.out.println("注册成功，请牢记用户名和密码。");
            System.out.println("请按任意键继续...");
        }
    }
}