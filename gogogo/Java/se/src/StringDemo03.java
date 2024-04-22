public class StringDemo03 {
    public static void main(String[] args) {
        /*  
        substring(int start,int end)
        取出当前字符串第start到end-1的字符串（不含end）
        char charAt(int index)
        返回当前字符串中的第index个字符
        String trim()
        去除字符串前后的空格

        //substring(int start,int end)
         */
        String url="www.google.com";
        int start=url.indexOf(".");
        int end=url.indexOf(".",start+1);
        String str=url.substring(start+1,end);
        System.out.println(str);
        System.out.println("--------------");
        //char charAt(int index)
        char chr=url.charAt(0);
        System.out.println(chr);
        //String trim()
        String ur12=" www.google.com  ff";
        System.out.println("------------");
        System.out.println(ur12);
        System.out.println(ur12.trim());
        String str1="上海自来水来自海上";
        boolean is=true;
        for (int i = 0; i < str1.length()/2; i++) {
            char f=str1.charAt(i);
            char e=str1.charAt(str1.length()-1-i);
            System.out.println(f);
            System.out.println(e);
            if (f!=e) {
                is=false;
                break;
                
            }
        }
        System.out.println(is?"是回文":"不是回文");
}
}
