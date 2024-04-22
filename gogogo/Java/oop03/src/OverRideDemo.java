public class OverRideDemo {
    public static void main(String[] args) {
        // TODO Auto-generated method stub 
        //重写
        //构造方法的快捷方式
        Person p1=new Person();
        p1.say();
        Person p2=new Person();
        //p2伪装父类
        p2.say();
        //重写，在两个类中，在父子类中，方法名相同，参数相同，子类方法重写了父类方法
        //也就是子类把父类的东西重新定义了一遍
        //
        /*
         * 
     (1)重载
        1.在同一类中
        2.方法名相同
        3.参数列表不同
        4.重载遵循编译器绑定
        5.根据参数列表调用
     (2)重写
        1.父子类(子类方法重写父类方法)
        2.方法名相同
        3.参数列表相同
        4.遵循运行期绑定（运行后出结果）
        5.根据对象的类型决定调用
         * 
         */
    }
}
