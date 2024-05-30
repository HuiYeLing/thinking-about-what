
public class KnitHat extends Hat {
    private String stuff;

    public KnitHat() {
    }

    public KnitHat(String type, String quarter, String stuff) {
        super(type, quarter);
        this.stuff = stuff;
    }

    public String getStuff() {
        return stuff;
    }

    public void setStuff(String stuff) {
        this.stuff = stuff;
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("原材料：" + stuff);
    }
}