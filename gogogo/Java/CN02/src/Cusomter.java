import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.HashSet;
import java.util.Set;
import java.util.Map;
import java.util.Iterator;
import java.util.Collection;

public class Cusomter {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add("aa");
        list.add("bb");
        list.add("cc");
        System.out.println(list);
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
        System.out.println("---------------");
        Set set = new HashSet();
        set.add("A");
        set.add("B");
        set.add("C");
        //普通for循环
        //for (Object obj : set) {
        //    System.out.println(obj);
        //}
        System.out.println("增强版for循环");
        for(Object a:list)//定义一个Object类型的变量a，用来接收list中的元素
            System.out.println(a);
        for(Object b:set)
            System.out.println(b);

        System.out.println("迭代器");
        System.out.println("list集合的迭代器");
        Iterator iterator = set.iterator();
        while (iterator.hasNext()) 
            System.out.println(iterator.next());
            
        HashMap map=new HashMap();
        //向map中添加元素,key和value都可以是任意类型的数据
        map.put("s01","张三");
        map.put("s02","李四");
        map.put("s03","王五");
        Set set2=map.keySet();//把map中所有的key存入set集合中
        for(Object c:set2)
            {
                System.out.println(c);
                System.out.println(c+" "+map.get(c));
            }
        System.out.println("entry遍历");
        Set entrySet=map.entrySet();
        for(Object obj:entrySet)
            {
                Map.Entry entry=(Map.Entry)obj;
                System.out.println(entry.getKey()+" "+entry.getValue());
            }
    }
}
