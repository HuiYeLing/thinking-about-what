import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Demo{
    public static void main(String[] args) throws Exception {
        List<Person> persons = new ArrayList<Person>();
        Person p1 = new Person("张三", 18, "浙江");
        Person p2 = new Person("李四", 19, "江苏");
        Person p3 = new Person("王五", 20, "上海");
        persons.add(p1);
        persons.add(p2);
        persons.add(p3);
    }
}

class Person {
    private String name;
    private int age;
    private String address;

    public Person(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }
}
