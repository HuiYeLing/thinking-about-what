import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
public class CollectionDemo {
    public static void main(String[] args) {
        List<String> list=new ArrayList();
        list.add("a");
        list.add("d");
        list.add("b");
        list.add("x");
        list.add("c");
        Collections.sort(list);//默认字典排序
        System.out.println(Collections.max(list));
        System.out.println(Collections.min(list));

        //查找一个元素
        //二分法查找 binarySearch()使用前必须保证集合元素是自然有序的
        System.out.println(Collections.binarySearch(list, "b"));
        //shuffle()打乱集合中元素的顺序
        Collections.shuffle(list);
        System.out.println(list);
        //swap()交换集合中的两个元素
        Collections.swap(list, 0, 4);
        System.out.println(list);
        //将集合中的a替换为A
        Collections.replaceAll(list, "a", "A");
        System.out.println(list);
        //将集合中的所有元素替换为A
        Collections.fill(list, "A");
        System.out.println(list);
    }
}
