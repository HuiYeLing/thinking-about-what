public class BZL {

    public static void main(String[] args) {
        int i=10;
        Integer j=new Integer(20);
        i=j;//将Integer类型的对象赋值给int类型的变量 自动拆箱 底层调用intValue()方法
        j=i;//将int类型的变量赋值给Integer类型的对象 自动装箱 底层调用Integer.valueOf(i)方法

        Integer i1=100;//自动装箱
        Integer i2=100;//自动拆箱
        Integer i3=1000;//自动装箱
        Integer i4=1000;//自动装箱
        System.out.println(i1==i2);
        System.out.println(i3==i4);

        
    }
}