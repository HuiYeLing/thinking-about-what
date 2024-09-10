import java.util.concurrent.ThreadLocalRandom;

public class 数组 {
    public static void main(String[] args) throws Exception {
        int[] arr = new int[5];
        int[] nums = {1, 3, 2, 5, 4};
        // 初始化数组

        数组 app = new 数组();// 创建App对象
        int randomNum = app.randomAccess(nums);// 随机抽取一个数字
        System.out.println("随机抽取的数字是: " + randomNum);// 输出随机抽取的数字
    }

    // 随机访问数组元素
    public int randomAccess(int[] nums) {
        // 在0到nums.length之间随机抽取一个数字
        int randomIndex = ThreadLocalRandom.current().nextInt(0, nums.length);
        // 获取并返回随机元素
        return nums[randomIndex];
    }

    // 插入元素
    // 在数组的索引index处插入元素num
    void insert(int[] nums, int num, int index) {
        // 把索引index以及之后的所有元素都向后移动一位
        for (int i = nums.length - 1; i >= index; i--) {
            nums[i] = nums[i - 1];
        }
        // 把num插入到索引index处
        nums[index] = num;
    }

    // 删除元素
    void remove(int[] nums, int index) {
        // 把索引index之后的所有元素都向前移动一位
        for (int i = index; i < nums.length - 1; i++) {
            nums[i] = nums[i + 1];
        }
    }

    // 遍历数组
    void traverse(int[] nums) {
        int count = 0;
        // for循环遍历数组
        for (int i = 0; i < nums.length; i++) {
            count += nums[i];
        }
        System.out.println("数组元素的总和是: " + count);
    }

    // 查找元素
    int find(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target)
                return i;
        }
        return -1;
    }

    // 扩容数组
    int[] extend(int[] nums, int enlarge) {
        int[] res = new int[nums.length + enlarge];
        // 把nums中的所有元素复制到res中
        for (int i = 0; i < nums.length; i++) {
            res[i] = nums[i];
        }
        return res;
    }
}