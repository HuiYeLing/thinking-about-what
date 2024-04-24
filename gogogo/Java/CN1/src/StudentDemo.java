public class StudentDemo {
    public static void main(String[] args) {
        StudentBize stuBize=new StudentBize();
        Student stu1=new Student();
        stu1.setName("张三");
        stu1.setAge(23);
        stuBize.addStudent(stu1);

        Student stu2=new Student();
        stu2.setName("李四");
        stu2.setAge(12);
        stuBize.addStudent(stu2);

        Student stu3=new Student();
        stu3.setName("王五");
        stu3.setAge(32);
        stuBize.addStudent(stu3);
        stuBize.showStudent();
    }
}
