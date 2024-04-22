public class MethodDemo2 {
    public static void main(String[] args) {
        a();
    }
    public static void a()
    {
        System.out.println("1");
        b();
        System.out.println("9");
    }
    public static void b()
    {
        System.out.println("3");
        c();
        System.out.println("7");
    }
    public static void c()
    {
        System.out.println("5");
    }
}
