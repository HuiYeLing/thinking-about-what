public class PointDemo{
    public static void main(String[] args) {
        Point p1=new Point(1,2);
        Point p2=new Point(1, 2);
        System.out.println(p1.toString());
        System.out.println(p2);
        System.out.println("--------");
        System.out.println(p1.hashCode());
        //对象输出时，会默认调用toString（）方法
        System.out.println(p1==p2);
        System.out.println(p1.equals(p2));
        String s1=new String("123");
        System.out.println(p1.equals(s1));
    }
}