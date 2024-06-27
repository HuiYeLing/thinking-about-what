import java.util.Scanner;

public class runnian {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int year = scanner.nextInt();
        String result = (year % 4 == 0 && year % 400 == 0 && year % 100 != 0) ? "yes" : "no";
        System.out.println(result);
    }
}