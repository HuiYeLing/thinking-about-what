package example;

public class TestPoint {
    public static void main(String[] args){
    //
    Point<Integer,Integer>p1 = new Point<Integer,Integer>();
    p1.setX(100);
    p1.setY(200);
    System.out.println("坐标:"+p1.getX()+","+p1.getY());
    Point<String,Double>p2 = new Point<String,Double>();
    p2.setX("东经38.5度");
    p2.setY(23.8);
    System.out.println("坐标:"+p2.getX()+","+p2.getY());
}
}
