import java.util.Random;

public class EqualsDemo {
    public static void main(String[] args) {
        Random rand = new Random();
        int num1 = rand.nextInt(241) + 20; // 生成[20,260]的随机数
        int num2 = rand.nextInt(241) + 20; // 生成[20,260]的随机数
        System.out.println(num1);
        System.out.println(num2);
        if (num1 == num2) {
            System.out.println("相等");
        } else {
            System.out.println("不相等");
        }
    }
}