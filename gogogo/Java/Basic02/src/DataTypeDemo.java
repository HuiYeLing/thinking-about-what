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

        // �ʺű��ʽ
        // ����ѡ����� ���1 �����2 ���ʽ���Ϊ�棬���ؽ��1��ֵ�����򷵻ؽ��2��ֵ  ѡ�����if
        // ���� 3��5 �ѽϴ�ķŵ�max��
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