import java.util.Arrays;
import java.util.Scanner;

public class dafen {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] finalScores = new double[5]; // 存储5位选手的最终得分
        double maxScore = 0; // 存储最高分
        int championIndex = 0; // 存储冠军的索引

        for (int j = 0; j < 5; j++) { // 对每位选手进行评分
            int[] scores = new int[6]; // 存储6个评委的打分
            System.out.println("选手" + (j + 1) + "的评分：");
            for (int i = 0; i < 6; i++) {
                System.out.println("请输入第" + (i + 1) + "个评委的打分（0~100）：");
                scores[i] = scanner.nextInt();
            }
            finalScores[j] = calculateFinalScore(scores); // 计算最终得分
            System.out.println("选手" + (j + 1) + "的最终得分是：" + finalScores[j]);

            // 更新最高分和冠军的索引
            if (finalScores[j] > maxScore) {
                maxScore = finalScores[j];
                championIndex = j;
            }
        }

        // 输出冠军信息
        System.out.println("冠军是选手" + (championIndex + 1) + "，得分：" + maxScore);
    }

    // 计算最终得分的方法
    public static double calculateFinalScore(int[] scores) {
        Arrays.sort(scores); // 对评分进行排序
        int sum = 0;
        for (int i = 1; i < scores.length - 1; i++) {
            sum += scores[i];
        }
        return sum / 4.0; // 返回4个评分的平均值
    }
}