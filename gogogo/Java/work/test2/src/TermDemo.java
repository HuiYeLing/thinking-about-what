
import java.util.Random;
import java.util.Arrays;
import java.util.Collections;

public class TermDemo {
    public static void main(String[] args) {
        Integer arr[] = new Integer[50];
        Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = random.nextInt(101);
        }
        Arrays.sort(arr, Collections.reverseOrder());
        System.out.println(Arrays.toString(arr));
    }
}