import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class 列表 {
    // 无初始值的列表
    List<Integer> nums1 = new ArrayList<>();
    // 有初始值的列表
    Integer[] numbers = new Integer[]{1, 2, 3, 4, 5};
    List<Integer> nums = new ArrayList<>(Arrays.asList(numbers));

    // 列表的本质是数组
    // 访问元素
    int num = nums.get(1);
    // 访问索引为1的元素

    // 更新元素
    nums.set(1, 0);
    // 把索引为1的元素更新为0

    // 清空列表
    nums.clear();

    // 在尾部添加元素
    nums.add(1);
    nums.add(3);
    nums.add(2);
    nums.add(5);
    nums.add(4);

    // 在中间插入元素
    nums.add(3, 6); // 在索引为3的位置插入元素6

    // 删除元素
    nums.remove(3); // 删除索引为3的元素

    // 遍历列表
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        count += nums.get(i);
    }

    // 直接遍历
    for (int num : nums) {
        count += num;
    }

    // 拼接列表
    List<Integer> nums2 = new ArrayList<>(Arrays.asList(new Integer[]{6, 8, 7, 10, 9}));
    nums.addAll(nums2); // 把nums2的元素拼接到nums后面

    // 排序列表
    Collections.sort(nums); // 排序后，列表元素从小到大排列
}