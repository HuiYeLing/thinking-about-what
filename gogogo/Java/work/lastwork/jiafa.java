import java.util.Scanner;
import java.util.Random;
public class jiafa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        System.out.println("请输入要做的式子数量");
        int count = sc.nextInt();//输入要做的式子数量
        int score = 0;//记录分数
        for (int i = 0; i < count; i++) {
            int a = random.nextInt(16);
            int b = random.nextInt(16);
            
            int answer = sc.nextInt();
            if (answer == a + b) {
                System.out.println("回答正确");
                score++;
            } else {
                System.out.println("回答错误");
            }
        }
        System.out.println("你的分数是：" + score);
    }
}
