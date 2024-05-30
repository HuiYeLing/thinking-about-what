import java.util.Random;

public class BiggerDemo {
    public static void main(String[] args) {
        Random random = new Random();
        int randomNumber1 = 25 + random.nextInt(101);  
        int randomNumber2 = 25 + random.nextInt(101);  
        System.out.println("随机数1：" + randomNumber1);
        System.out.println("随机数2：" + randomNumber2);
        if (randomNumber1 > randomNumber2) {
            System.out.println("较大的数是：" + randomNumber1);
        } else {
            System.out.println("较大的数是：" + randomNumber2);
        }
    }
}