public class Person {
    public String name;
    int age;
    protected long phonenumber;//�ܱ���������
    private String address;//˽������
    // ���캯��
    public Person(){
        super();
        this.name = "����";
        this.age = 18;
        this.phonenumber = 123456789;
        this.address = "������";
    }
    public void setAddress(String address){
        this.address = address;
    }
    public String getAddress(){
        return address;
    }
}
