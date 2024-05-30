
public class Earring {
    private String type;
    private String color;
    private String brand;

    public Earring() {
        super();
    }

    public Earring(String type, String color, String brand) {
        this.type = type;
        this.color = color;
        this.brand = brand;
    }

    public void show() {
        System.out.println("太阳光下很漂亮");
    }

    public void showInfo() {
        System.out.println("样式：" + type);
        System.out.println("颜色：" + color);
        System.out.println("品牌：" + brand);
    }
}
