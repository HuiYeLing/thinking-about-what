public class Person {
    public String name;
    int age;
    protected long phonenumber;//受保护的属性
    private String address;//私有属性
    // 构造函数
    public Person(){
        super();
        this.name = "张三";
        this.age = 18;
        this.phonenumber = 123456789;
        this.address = "北京市";
    }
    public void setAddress(String address){
        this.address = address;
    }
    public String getAddress(){
        return address;
    }
}
