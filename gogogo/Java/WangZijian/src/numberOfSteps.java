import java.util.Scanner;

public class numberOfSteps {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        Solution solution = new Solution();
        int count = solution.numberOfSteps(num);
        System.out.println("步数: " + count);
    }
}

class Solution {
    public int numberOfSteps(int num) {
        int count = 0;
        while (num != 0) {
            if (num % 2 == 0) {
                num = num / 2;
            } else {
                num = num - 1;
            }
            count++;
        }
        return count;
    }
}