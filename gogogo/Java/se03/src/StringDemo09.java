public class StringDemo09 {
    public static void main(String[] args) {
        //将当前字符串中的数字替换成“数字”w
        //String replaceAll(String regex,String str)
        String str="a2adaqeq5123didq677675fa33";
        // \d表示数字，+表示出现一次或多次
        String regex="\\d+";
        String str1=str.replaceAll(regex, "数字");
        System.out.println(str1);

        //和谐器
        String str2="java,你是sb";
        String regex1="sb|操|草|日|妈|傻|逼";//词库
        String str3=str2.replaceAll(regex1, "**");
        System.out.println(str3);
        String str4=str2.toLowerCase().replaceAll(regex1, "**");
        System.out.println(str4);

    }
}
