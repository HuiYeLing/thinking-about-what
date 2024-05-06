class Rope {
    private String type;
    private String size;

    public Rope(String type, String size) {
        this.type = type;
        this.size = size;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public void showInfo() {
        System.out.println("类型: " + type + ", 尺寸: " + size);
    }
}


class JumpRope extends Rope {
    private String color;

    public JumpRope() {
        super("",
         ""); 
    }

    public JumpRope(String type, String size, String color) {
        super(type, size);
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public void showInfo() {
        super.showInfo();
        System.out.println("颜色: " + color);
    }
}

public class JumpRopeDemo {
    public static void main(String[] args) {
        JumpRope  jumpRope = new JumpRope("绳子", "1.5m", "黑色"); 
        jumpRope.showInfo();
    }
    
}