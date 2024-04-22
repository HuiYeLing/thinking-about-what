public  class Son{
    //子类继承父类，extends
    String name;
    int age;
    Son()
    {
        age=18;
        name="张三";
    }
    Son(int a,String n)
    {
        age=a;
        name=n;
    }
    void sayHi()
    {
        System.out.println(name+age);
    }
    void spend()
    {
        
    }
}