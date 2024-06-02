
public class Person {
    //name age city 私有 +构造函数+setget
    private String name;
    private int age;
    private String city;
    private int id;
    public Person() {
        super();
    }

    public Person(String name, int age, String city, int id) {
        this.name = name;
        this.age = age;
        this.city = city;
        this.id = id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void setCity(String city) {
        this.city = city;
    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public String getCity() {
        return city;
    }
   public String toString() {
        return "Person [id="+id+",name=" + name + ", age=" + age + ", city=" + city + "]";
    }


}
