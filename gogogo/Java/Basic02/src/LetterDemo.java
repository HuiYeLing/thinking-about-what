public class LetterDemo {
    public static void main(String[] args) {
        int num = (int) (Math.random()*26);//[0,25]
        // ����һ������Ĵ�д��ĸ
        char ch=(char)('A'+num);//������ת��Ϊ�ַ�
        System.out.println(num+" "+ch);
        
    }
}
