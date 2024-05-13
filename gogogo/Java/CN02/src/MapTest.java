import java.util.HashMap;
import java.util.Set;
import java.util.Collection;
import java.util.Map;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.HashSet;

public class MapTest {
    public static void main(String[] args) {
        // Your code here
        HashMap map=new HashMap();
        //向map中添加元素,key和value都可以是任意类型的数据
        map.put("s01","张三");
        map.put("s02","李四");
        map.put("s03","王五");
        System.out.println(map);
        //get()方法获取指定key对应的value
        System.out.println(map.get("s01"));
        //元素个数size()
        System.out.println(map.size());
        //判断是否包含指定key
        //containsKey()方法
        System.out.println(map.containsKey("s01"));
        System.out.println(map.containsValue("王五"));
        System.out.println("-------------------");
        Set set=map.keySet();//把map中所有的key存入set集合中
        System.out.println(set);
        Collection values=map.values();//把map中所有的value存入Collection集合中
        System.out.println(values);
        map.remove("s01");//删除指定key对应的元素
        map.remove("s013");//删除不存在的key对应的元素
        Object a=map.remove("s01");//删除指定key对应的元素，并返回删除的元素
        System.out.println(map);
        System.out.println(a);
    }
}