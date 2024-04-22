public class UpDemo {
    public static void main(String[] args) {
        Animal a=new Animal();
        System.out.println(a.age);
        a.eat();
        Tiger t=new Tiger();
        System.out.println(t.name);
        t.say();
        t.eat();

        System.out.println(t.age);//子类对象可以调用父类中的属性
        Animal a1=new Tiger();//向上转型，自动转型，父类引用指向子类对象
        //a1就是一个Animal对象，所以只能调用Animal类中的方法
        a1.eat();
        System.out.println(a1.age);
        //a1.say();//错误，因为a1是Animal类型的，而Animal类中没有say()方法
        
        Object o=new Tiger();
    }
}
