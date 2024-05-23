
public class Student implements Comparable<Student>{

    private int id;
    private String name;
    private int age;
    private String city;

    public Student() {
        
    }

    public Student(int id, String name, int age, String city) {
        
        this.id = id;
        this.name = name;
        this.age = age;
        this.city = city;
    }

    public int getId() {
        return id;
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

    public void setId(int id) {
        this.id = id;
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
    public String toString() {
        return "student [id=" + id + ", name=" + this.name + ", age=" + this.age + ", city=" + this.city + "]";
    }
    //重写比较器接口中的方法
    @Override
    public int compareTo(Student o) {
        //方法默认是升序
        Student in = o;
        //根据学号 降序
        int res = this.id < in.id ? 1 : (this.id == in.id ? 0 : -1);
        //如果学号相同，按照年龄升序
        if (res == 0) {
            res = this.name.compareTo(in.name);
        }
        return res;
    }
}   
