import java.util.Arrays;
import java.util.Random;

public class ValueDemo {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] prices = new int[10];
        for (int i = 0; i < prices.length; i++) {
            prices[i] = 50 + rand.nextInt(251); // 修复这里
        }
        Arrays.sort(prices);
        for (int price : prices) {
            System.out.println(price);
        }
    }
}