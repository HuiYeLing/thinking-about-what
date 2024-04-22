public class StringDemo06 {
    public static void main(String[] args) {
        //TODO Auto-generated method stub
        //检验用户名和密码是否符合规范
        /*
         * Boolean matches(String regex)
         * 使用给定的正则表达式验证当前字符串是否符合规范
         *  
         * 第一步：regex
         * \w : 数字和字母至少有一个
         * +：表示有若干个
         */


         String mailregex="\\w+@\\w+(\\.\\w+)+";
         String mail="soft0101@163.com.cn";
         System.out.println(mail.matches(mailregex));
    }
}
