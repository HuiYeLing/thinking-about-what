public class Teacher {
    String name;// data member
    int age;// data member
    String address;// data member
    double salary;

    void eat()
    {
        System.out.println(name+" is eating");
    }
    void sleep()
    {
        System.out.println(name+" is sleeping");
    }
    void info()
    {
        System.out.println("我叫"+name+",今年"+age+"岁,住在"+address+",工资是"+salary+"元");
    }
}
