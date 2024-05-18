import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class test03 {
    public static void main(String[] args) {
        //根据人的名字查询信息
        
        class Person {
            private String name;
            private int age;
            private String city;

            public Person(String name, int age, String city) {
                this.name = name;
                this.age = age;
                this.city = city;
            }

            // getters and setters

            @Override
            public String toString() {
                return "Person [name=" + name + ", age=" + age + ", city=" + city + "]";
            }
        }

        Person p1 = new Person("张三", 23, "北京");
        Person p2 = new Person("李四", 24, "上海");
        Person p3 = new Person("王五", 25, "广州");
        //key是姓名，value是Person对象
        Map<String,Person> map = new HashMap();
        map.put("张三", p1);
        map.put("李四", p2);
        map.put("王五", p3);

        //根据名字查询信息
        System.out.println("请输入人的名字");
        Scanner sc = new Scanner(System.in);

        String name = sc.next();
        System.out.println(map.get(name).toString());
        


        // Set<String> names=map.keySet();
        // for (String n : names) {
        //     if(name.equals(name)){//找到这个人的姓名
        //         System.out.println(map.get(name).toString());
        //     }
        // }
        
    }
}
