import java.util.Scanner;
public class TeacherDemo {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        //����ĳһ����Ķ���ĸ�ʽ
        //���� ������=new ����();
        Teacher t1=new Teacher(); // Use the imported Teacher class
        //Ϊĳһ��������и���ֵ ʵ����
        t1.name="����";
        t1.age=30;
        t1.address="����";
        t1.salary=10000;
        t1.eat();
        t1.sleep();
        t1.info();

        Teacher t2=new Teacher();
        t2.name="����";
        t2.age=20;
        t2.address="������";
        t2.salary=20000;
        t2.eat();
        t2.sleep();
        t2.info();

        Teacher t3;
        t3=t1;
        t3.eat();
        t3.name="����";
        t1.eat();
        t3.eat();

        Teacher t4=new Teacher();
        t4.name="��5";
        t4.age=40;
        t4.address="�Ϻ�";
        t4.salary=30000;
        
        System.out.println(t1==t4);
        System.out.println(t1==t3);
    }
}
