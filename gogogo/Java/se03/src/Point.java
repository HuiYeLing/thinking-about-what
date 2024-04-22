public class Point {
    private int x;
    private int y;
    public Point() {
        super();
    }
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    //set和get
    public int getX() {
        return x;
    }
    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }
    public void setY(int y) {
        this.y = y;
    }  
    public String toString()
    {
        return "("+this.x+","+this.y+")";
    }
    public boolean equals(Object obj)
    {
        if(obj==null)
        {
            //对于非空x，x.equals(null) ,返回false
            return false;
        }
        if(this==obj)
        {
            return true;
        }
        if(obj instanceof Point)
        {
            Point p=(Point)obj;
        }
        return false;
    }
}
