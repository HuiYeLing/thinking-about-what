 class Book{
    private String size;
    private String color;

    public Book() {
        super();
    }

    public Book(String size, String color) {
        this.size = size;
        this.color = color;
    }

    public void read() {
        System.out.println("书本用来读的。");
    }

    public void showInfo() {
        System.out.println("尺寸: " + size + ", 颜色: " + color);
    }
}

public class  Main {
    public static void main(String[] args) {
        Book book = new Book("A4", "蓝色");
        book.read();
        book.showInfo();
    }
    
}