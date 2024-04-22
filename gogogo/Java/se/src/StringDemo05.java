public class StringDemo05 {
    public static void main(String[] args) {
        int i=123;
        String istr=String.valueOf(i);
        System.out.println(istr);
        //StringBuilder:内部维护一个可变的字符数组
        StringBuilder b1=new StringBuilder("努力学习java");
        System.out.println(b1);
        b1.append("走上人生巅峰");
        System.out.println(b1.toString());
        //replace(int start,int end)
        //将start到end-1的字符替换为指定的字符串
        b1.replace(7, b1.length(), "成为fullstack工程师");
        System.out.println(b1);
        //插入
        //insert(int offset,String str)
        //在指定位置插入字符串
        b1.insert(7, "认真");
        System.out.println(b1);
        //reverse()：没有参数
        //将字符串反转
        b1.reverse();
        System.out.println(b1);
    }
}
