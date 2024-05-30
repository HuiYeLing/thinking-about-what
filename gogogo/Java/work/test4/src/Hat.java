
public class Hat {
    private String type;
    private String quarter;

    public Hat() {
    }

    public Hat(String type, String quarter) {
        this.type = type;
        this.quarter = quarter;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getQuarter() {
        return quarter;
    }

    public void setQuarter(String quarter) {
        this.quarter = quarter;
    }

    public void showInfo() {
        System.out.println("样式：" + type);
        System.out.println("适用季度：" + quarter);
    }
}