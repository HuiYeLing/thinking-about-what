public class Person {
    String name;
    int age;
    Person() {
        name = "张三";
        age = 18;
    }
    Person(String n, int a) {
        //this指代当前对象
        this.name = n;
        this.age = a;
    }
    void say() {
        System.out.println("姓名：" + name + "，年龄：" + age);
    }
}

