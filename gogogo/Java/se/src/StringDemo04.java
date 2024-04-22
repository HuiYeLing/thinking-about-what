public class StringDemo04 {
    public static void main(String[] args) {
     /*
        boolean startwith(String str)
        判断当前字符串是不是以给定字符串开头的
        boolean endwith(String str)
        判断当前字符串是不是以给定字符串结尾的
        boolean toUpperCase()
        将当前字符串转换为大写
        boolean toLowerCase()
        将当前字符串转换为小写
      */
      String url="www.google.com";
      boolean start=url.startsWith("www");
      System.out.println(start);
        boolean end=url.endsWith(".co");
        System.out.println(end);
        System.out.println("---------------");
        System.out.println(url);
        System.out.println(url.toLowerCase());
        System.out.println(url.toUpperCase());
    }
}
