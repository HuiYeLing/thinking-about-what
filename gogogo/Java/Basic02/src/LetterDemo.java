public class LetterDemo {
    public static void main(String[] args) {
        int num = (int) (Math.random()*26);//[0,25]
        // 生成一个随机的大写字母
        char ch=(char)('A'+num);//将数字转化为字符
        System.out.println(num+" "+ch);
        
    }
}
