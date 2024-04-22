public class DataTypeDemo {
    public static void main(String[] args) throws Exception {
        long b = 10000000;
        int a = (int) b;
        char ch = 'a';
        System.out.println(ch);
        System.out.println((int) ch);
        boolean b1 = true;
        System.out.println(b1);
        System.out.println(5 / 2);
        System.out.println(5.0 / 2);

        // 问号表达式
        // ？：选择语句 结果1 ：结果2 表达式如果为真，返回结果1的值，否则返回结果2的值  选择语句if
        // 两个 3和5 把较大的放到max中
        int max = 3 > 5 ? 3 : 5;
        System.out.println(max);
        int a2 = 3, b2 = 5;
        int max1 = a2 > b2 ? a2 : b2;
        System.out.println(max1);
        int num = (int) (Math.random() * 10);
        System.out.println(num);
        int num1 = (int) (Math.random() * 11 + 10);
        System.out.println(num1);
    }
}