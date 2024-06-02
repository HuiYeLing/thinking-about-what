
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.Panel;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.logging.Formatter;
import java.util.logging.LogRecord;


class SnakeClient extends Frame {
    Snake mySnake = new Snake(this);
    Food myFood = new Food(this);

    //创建label控件作为计分板

    Label lbl = new Label("你已经吃了"+mySnake.eatEggs+"个蛋");
    //新建容器
    Panel p = new Panel();

    public SnakeClient() {
        //绘制地图窗体
        this.setBounds(0,0,900,800);
        this.setTitle("贪吃蛇");//设置标题
        this.setBackground(Color.BLACK);//设置背景颜色
        //点击叉号关闭窗体
        this.addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent e){
                System.exit(-1);
            }
        }); 
        setResizable(false);


        //加入得分信息
        lbl.setAlignment(1);
        p.add(lbl);
        p.setBackground(Color.GREEN);//设置背景颜色
        this.setLayout(new GridLayout(7,1,50,80));//设置布局,7行1列
        p.setLayout(new GridLayout(1,1));//设置布局,1行1列
        this.add(p);
        this.setVisible(true);//设置窗体可见
    }

    //开启线程和打开键盘监视
    public void launch(){
        this.addKeyListener(new KeyMonitor());//添加键盘监视
        new Thread(new PaintThread()).start();//开启线程
    }

    public void paint(Graphics g){
        mySnake.paint(g);//画蛇
        myFood.paint(g);//画食物
    }

    //线程控制
    class PaintThread implements Runnable{
        public void run(){
            //保持线程一直运行
            while(true){
                // Fix: Call repaint on SnakeClient instance
                SnakeClient.this.repaint();//重绘
                try {
                    Thread.sleep(90);//休眠100毫秒
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    //键盘监视
    class KeyMonitor extends KeyAdapter{
        public void keyPressed(KeyEvent e){
            // Fix: Call keyPressed on mySnake instance
            mySnake.keyPress(e);//键盘按下
        }
    }

    public static void main(String[] args) 
    {
        SnakeClient sc = new SnakeClient();
        sc.launch();
    }
}