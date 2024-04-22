import java.util.Scanner;
public class TeacherDemo {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        //创建某一个类的对象的格式
        //类名 对象名=new 类名();
        Teacher t1=new Teacher(); // Use the imported Teacher class
        //为某一个对象进行赋初值 实例化
        t1.name="张三";
        t1.age=30;
        t1.address="北京";
        t1.salary=10000;
        t1.eat();
        t1.sleep();
        t1.info();

        Teacher t2=new Teacher();
        t2.name="李四";
        t2.age=20;
        t2.address="提瓦特";
        t2.salary=20000;
        t2.eat();
        t2.sleep();
        t2.info();

        Teacher t3;
        t3=t1;
        t3.eat();
        t3.name="王五";
        t1.eat();
        t3.eat();

        Teacher t4=new Teacher();
        t4.name="赵5";
        t4.age=40;
        t4.address="上海";
        t4.salary=30000;
        
        System.out.println(t1==t4);
        System.out.println(t1==t3);
    }
}
