import java.util.ArrayList;
import java.util.List;
public class ListTest {
    public static void main(String[] args) {
        List list1 = new ArrayList(); //创建对象list1
        System.out.println(list1);
        list1.add("a");//向list1中添加元素
        list1.add("b");
        list1.add("c");
        System.out.println(list1);
        list1.add( "d");
        System.out.println(list1);
        list1.add(1, "e");
        //在list1的第二个位置添加元素e
        //add(index, element)方法在指定位置添加元素
        System.out.println(list1);
        List list2 = new ArrayList();//创建对象list2
        list2.add("1");
        list2.add("2");
        System.out.println(list2);//输出list2
        //addAll()方法将list2中的元素全部添加到list1中
        //addAll(index, collection)方法将指定集合中的元素添加到指定位置
        list1.addAll(2, list2);
        System.out.println(list1);
        //get(index)方法获取指定位置的元素
        System.out.println(list1.get(1));
        //indexOf()方法获取指定元素的位置
        list1.add("e");
        System.out.println(list1.indexOf("e"));
        
        //lastIndexOf()方法获取指定元素的最后一个位置
       
        System.out.println(list1);
        System.out.println(list1.lastIndexOf("e"));
        //set(index, element)方法修改指定位置的元素
        list1.set(1, "中");
        System.out.println(list1);
        //subList(fromIndex, toIndex)方法截取指定范围的元素
        System.out.println();
    }
}
