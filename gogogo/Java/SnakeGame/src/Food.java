
import java.util.Random;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

class Food {

    public static int WIDTH = 20;
    public static int HEIGHT = 20;
    int x,y;
    SnakeClient ms;
    Random rd = new Random();

    public Food(SnakeClient ms)
    {
        reFood();//初始化食物
        this.ms = ms;
    }

    public void reFood()
    {
       
       int num2=rd.nextInt(877);
       if(num2<4)num2=num2+(4-num2);
        x = num2;
        int num=rd.nextInt(777);
        if(num<67)num=num+(67-num);
        y = num;
    }
    public int getX()
    {
        return x;
    }
    public void setX(int x)
    {
        this.x = x;
    }
    public int getY()
    {
        return y;
    }
    public void paint(Graphics g){
        g.setColor(Color.RED);
        g.fillRect(x, y, WIDTH, HEIGHT);
    }

    public Rectangle getRect()
    {
        return new Rectangle(x, y, WIDTH, HEIGHT);
    }
}