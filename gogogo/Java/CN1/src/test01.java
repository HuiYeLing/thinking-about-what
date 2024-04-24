import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class test01 {
    public static void main(String[]args){
        Collection co101=new ArrayList();
        co101.add("a");
        co101.add("b");
        co101.add("c");
        System.out.println(co101);
        co101.clear();
        System.out.println(co101);

        Student stu1=new Student();
        stu1.setName("张三");
        stu1.setAge(23);
        co101.add(stu1);

        Student stu2=new Student();
        stu2.setName("李四");
        stu2.setAge(12);
        co101.add(stu2);

        Student stu3=new Student();
        stu3.setName("王五");
        stu3.setAge(32);
        co101.add(stu3);
        System.out.println("-----------");
        System.out.println(co101);

        System.out.println(co101.size());
        Collection co102=new ArrayList();                                                                                                                                                                                                                                                                                    
        co102.add("a");
        co102.add("b");
        co102.add("c");
        System.out.println(co101);
        System.out.println(co102);
        co101.addAll(co102);
        System.out.println(co101);

        System.out.println(co101.contains("a"));
        System.out.println(co102.contains("D"));

        System.out.println("co101:"+co101);
        System.out.println("co102:"+co102);
        System.out.println(co101.containsAll(co102));

        System.out.println("co101是否为空:"+co101.isEmpty());
        co101.clear();
        System.out.println("co101是否为空:"+co101.isEmpty());

        Iterator iter=co101.iterator();
        while(iter.hasNext())
        {
           String result=(String)iter.next();
              System.out.println(result);   
        }

         co102.remove("b");
            System.out.println("co102"+co102);
            co101.add("a");
            co101.add("b");
            co101.add("c");
            System.out.println("co101"+co101);
            System.out.println("co102"+co102);
            co101.retainAll(co102);
            System.out.println("co101"+co101);
            System.out.println("co102"+co102);

            Object[] co101Array=co101.toArray();
            System.out.println(co101Array[0]);
            System.out.println(co101Array[1]);
            System.out.println(co101Array[2]);
    }
}
