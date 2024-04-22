import java.util.Scanner;
public class StudentDemo {
    public static void main(String[] args) {
        Student s1=new Student();
        s1.name="����";
        s1.age=20;
        s1.weight=60;
        s1.high=1.7;
        s1.run();
        s1.jump();
        System.out.println();
        System.out.println("����ͬ��ͬ��");
        System.out.println();
        Student s2=new Student();
        s2.name="����";
        s2.age=20;
        s2.weight=60;
        s2.high=1.7;
        s2.run();
        s2.jump();
        System.out.println();
        Student s3=new Student();
        s3=s1;
        System.out.println("");
        s3.name="����";
        s3.jump(); 
    }
}
