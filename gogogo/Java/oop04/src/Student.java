public class Student extends Person{
    public int grade;
    public Student(){

        this.grade = 111;
        this.name = "����";
        this.age=23;
        this.phonenumber = 123456789;
        //this.address = "������";//�޷�����
        this.setAddress("������");
        System.out.println(this.getAddress());
    }
}
