public class InDemo {
    public static void main(String[] args) {
        Person p = new Person();
        p.name="李四";
        p.age=20;
        p.phonenumber=987654321;
        //p.address="上海市";//无法访问
        p.setAddress("上海市");
        System.out.println(p.getAddress());
    }
}
