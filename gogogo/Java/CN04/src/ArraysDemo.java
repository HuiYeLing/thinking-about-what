import java.util.Arrays;

public class ArraysDemo {
    public static void main(String[] args) {
        int []arr =new int[] {3,2,14,16,6,1};
        //打印数组
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);

        }
        System.out.println("-----------------");
        //二分法查找
        System.out.println(Arrays.binarySearch(arr, 2));
        
    }
}
