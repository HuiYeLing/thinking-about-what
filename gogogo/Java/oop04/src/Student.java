public class Student extends Person{
    public int grade;
    public Student(){

        this.grade = 111;
        this.name = "张三";
        this.age=23;
        this.phonenumber = 123456789;
        //this.address = "北京市";//无法访问
        this.setAddress("北京市");
        System.out.println(this.getAddress());
    }
}
