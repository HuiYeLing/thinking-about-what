public class Demo {
    public static void main(String[] args) {
       
        System.out.println(Computer.price);
        Computer c1 = new Computer();
        System.out.println(c1.price);
        System.out.println(c1.color);
        Computer.say();
        c1.say();
    }
}
