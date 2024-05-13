import java.util.Collection;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.ArrayList;

public class Demo1 {
    public static void main(String[] args) {
        Collection list=new ArrayList();
        list.add("中国");
        list.add("美国");
        list.add("俄罗斯");
        System.out.println(list);

        Collection set=new HashSet();
        set.add("中国");
        set.add("美国");
        set.add("俄罗斯");
        System.out.println(set);

        LinkedList list2=new LinkedList();
        list2.add("hello");
        list2.add("world");
        list2.addFirst("hw");
        System.out.println(list2);
    }
}
