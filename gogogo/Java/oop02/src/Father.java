public class Father {
    int car;
    int house;
    int money;
    int book;

    Father(){
        car = 1;
        house = 1;
        money = 1000000;
        book = 100;
    }
    Father(int c,int h,int m, int b)
    {
        car = c;
        house = h;
        money = m;
        book = b;
    }
    void drive()
    {
        System.out.println("Father is driving a car");
    }
    void stay()
    {
        System.out.println("Father is living in a house");
    }
    void spend()
    {
        System.out.println("Father is spending money");
    }
    void read()
    {
        System.out.println("Father is reading a book");
    }
}
