public class StringDemo02{
    public static void main(String[] args) {
        //int length():返回字符串的长度
        //int indexOf(String str):返回str在字符串中第一次出现的位置
        String str1="你好，java";
        System.out.println(str1.length());
        System.out.println("--------------");
        String str2="thinking in java";
        System.out.println(str2.indexOf("in"));
        /*  
         * indexOf(String str);
         * indexOf(int ch);
         * indexOf(String str,int fromIndex);
         * indexOf(int ch,int fromIndex);
         */
        System.out.println(str2.indexOf("in",4));
        System.out.println(str2.indexOf("ink",4));
        System.out.println(str2.indexOf(str2));
        //查找一下str2中有几个in
        //只要index不等于-1，就一直找
        int index=0;
        int count=0;
        while(index!=-1)
        {
            index=str2.indexOf("in",index);
            if (index!=-1) {
                index=index+"in".length();
                count++;//从遭到的后一位再继续找下一次，找过的不能再找
            }
        }
        System.out.println(count);
    }
}
