import java.lang.reflect.Array;
import java.util.Arrays;

public class ArrayDemo {
    public static void main(String[] args) {
        //数组
        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * 100);
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);

            int max = 0;
            for (int j = 0; j < arr.length; j++) {
                if (arr[j] > max) {
                    max = i;
                    System.out.println("最大值为：" + arr[max]);
                    Arrays.sort(arr);
                    for(i=0;i<arr.length;i++){
                        System.out.println(arr[i]);
                    }
                }
            }
        }
    }
}
