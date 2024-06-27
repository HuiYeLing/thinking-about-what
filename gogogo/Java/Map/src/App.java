import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class App {
    public static void main(String[] args) throws Exception {
        // 创建一个Map集合
        Map<String, String> map = new HashMap<>();
        // 添加三行数据
        map.put("a", "1");
        map.put("b", "2");
        map.put("c", "3");
        // 使用迭代器遍历集合中的所有元素
        Iterator<Map.Entry<String, String>> iterator = map.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, String> entry = iterator.next();
            System.out.println(entry.getKey() + entry.getValue());
        }
    }
}