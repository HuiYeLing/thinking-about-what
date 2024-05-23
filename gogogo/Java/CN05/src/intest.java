import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class intest {
    public static void main(String[] args) {
        //内部比较器
        List<Person> persons = new ArrayList();
        Person p1=new Person(3,"张三",20,"北京");
        Person p2=new Person(1,"李四",22,"上海");
        Person p3=new Person(2,"王五",24,"广州");
        Person p4=new Person(4,"赵六",26,"深圳");
        persons.add(p1);
        persons.add(p2);
        persons.add(p3);
        persons.add(p4);
        //根据id排序
        //如果id相同，按照姓名升序
        Collections.sort(persons);
        System.out.println(persons);
        System.out.println("----------------------");
        //外部比较器
        List<Student> students = new ArrayList(); // Fix: Parameterize ArrayList with Student type
        Student s1 = new Student(3,"张三",20,"北京"); // Fix: Correct the class name to Student
        Student s2 = new Student(1,"李四",22,"上海"); // Fix: Correct the class name to Student
        Student s3 = new Student(2,"王五",24,"广州"); // Fix: Correct the class name to Student
        Student s4 = new Student(4,"赵六",26,"深圳"); // Fix: Correct the class name to Student
        students.add(s1); // Fix: Correct the variable name to students
        students.add(s2); // Fix: Correct the variable name to students
        students.add(s3); // Fix: Correct the variable name to students
        students.add(s4); // Fix: Correct the variable name to students

        Collections.sort(students,new MyComparator()); 
        System.out.println(students);
    }
}
