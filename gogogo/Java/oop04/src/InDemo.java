public class InDemo {
    public static void main(String[] args) {
        Person p = new Person();
        p.name="����";
        p.age=20;
        p.phonenumber=987654321;
        //p.address="�Ϻ���";//�޷�����
        p.setAddress("�Ϻ���");
        System.out.println(p.getAddress());
    }
}
