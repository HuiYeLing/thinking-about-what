public class Person {
    String name;
    int age;
    Person() {
        name = "����";
        age = 18;
    }
    Person(String n, int a) {
        //thisָ����ǰ����
        this.name = n;
        this.age = a;
    }
    void say() {
        System.out.println("������" + name + "�����䣺" + age);
    }
}

