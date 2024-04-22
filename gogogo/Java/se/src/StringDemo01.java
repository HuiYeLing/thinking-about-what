public class StringDemo01 {
    public static void main(String[] args) {

    
    String s1="123abc";
    String s2="123abc";
    String s3="123"+"abc";
    String s4="123";
    String s5=s4+"abc";
    String s6=1+"2"+"3abc";
    String s7=1+'2'+"3abc";
    String s8=new String("123abc");
    
        System.out.println("s1:"+s1);
        System.out.println("s2:"+s2);
        System.out.println("s3:"+s3);
        System.out.println("s4:"+s4);
        System.out.println("s5:"+s5);
        System.out.println("s6:"+s6);
        System.out.println("s7:"+s7);
        System.out.println("s8:"+s8);
        System.out.println("-----------------------");
        System.out.println(s1==s2);
        System.out.println(s1==s3);
        System.out.println(s1==s5);
        System.out.println(s1==s6);
        System.out.println(s1==s8);
}
}
