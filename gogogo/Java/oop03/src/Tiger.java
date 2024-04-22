public class Tiger extends Animal{
    String name;
    Tiger()
    {
        super();
        {
            name="老虎";
            System.out.println("我是老虎，我今年"+age+"岁了");
        }
    }
    Tiger(String n)
    {
        name=n;
    }
    void say()
    {
        System.out.println(name+" is eating");
    }
}
