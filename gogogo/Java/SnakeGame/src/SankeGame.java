
import java.util.LinkedList;
import java.util.Random;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.Color;
import java.awt.Rectangle;

class Snake {
    static LinkedList<SnakeBody> It=new LinkedList<SnakeBody>();
    SnakeBody sb;//蛇头
    int eatEggs=0;//吃的蛋的数量
    int number = 5;//蛇的长度
    boolean isLive ;//蛇是否活着 
    enum Direction{Left,Up,Right,Down};//枚举方向
    Random rd=new Random(); //随机数
    Direction snakeDirection;//默认方向
    SnakeClient sc = new SnakeClient();

    
    public Snake(SnakeClient sn)
    {
        //初始化蛇
        this.isLive = true;
        //初始化蛇身节点，头元素到尾元素从左到右
        for (int i = 0,bi=300; i <=number; i++,bi+=20) {
            It.add(new SnakeBody(bi, 300));
        }
        //初始化蛇身的前进方向，因为蛇头是集合尾部元素，所以蛇头的方向是向右
        //否则就咬到自己
        this.snakeDirection = Direction.Right;//默认方向
        this.sc = sn;//获得游戏界面
    }

    //蛇的移动
    //最后更新头部的位置，然后删除尾部的位置
    public void movel(){
        //如果蛇死了，就不再移动
        if(this.isLive==false){
            for(int i=0;i<It.size();i++)
            {
                It.get(i).x=It.get(i).x;//蛇的位置不变
                It.get(i).y=It.get(i).y;//蛇的位置不变
            }
        }
        //否则就判断移动方向并移动
        else{
            if (this.snakeDirection == Direction.Down) {
                for(int i=0;i<It.size();i++)
                {
                    if(i==It.size()-1)//如果是蛇头
                    {
                        It.get(i).y+=20;//一个身位， 固定20
                    }
                    else //非头元素
                    {
                        It.get(i).x=It.get(i+1).x;
                        It.get(i).y=It.get(i+1).y;
                    }
                }
            }
            else if (this.snakeDirection == Direction.Up) {
                for(int i=0;i<It.size();i++)
                {
                    if(i==It.size()-1)//如果是蛇头
                    {
                        It.get(i).y-=20;//一个身位， 固定20
                    }
                    else //非头元素
                    {
                        It.get(i).x=It.get(i+1).x;
                        It.get(i).y=It.get(i+1).y;
                    }
                }
            }
            else if(this.snakeDirection==Direction.Right)
                for(int i=0;i<It.size();i++){
                    if(i==It.size()-1)//如果是蛇头
                    {
                        It.get(i).x+=20;//一个身位， 固定20
                    }
                    else //非头元素
                    {
                        It.get(i).x=It.get(i+1).x;
                        It.get(i).y=It.get(i+1).y;
                    }
                }
            else if(this.snakeDirection==Direction.Left)
                for(int i=0;i<It.size();i++){
                    if(i==It.size()-1)//如果是蛇头
                    {
                        It.get(i).x-=20;//一个身位， 固定20
                    }
                    else //非头元素
                    {
                        It.get(i).x=It.get(i+1).x;
                        It.get(i).y=It.get(i+1).y;
                    }
                }
        }
    }

    int ti=0;//这个决定是否掉头，0否1是
    //执行掉头的中间操作
    public void huitou(){
        if(ti==1){
            switch (this.snakeDirection) {
                case Down:
                    this.snakeDirection = Direction.Up;
                    ti=0;
                    break;
                case Up:
                    this.snakeDirection = Direction.Down;
                    ti=0;
                    break;
                case Right:
                    this.snakeDirection = Direction.Left;
                    ti=0;
                    break;
                case Left:
                    this.snakeDirection = Direction.Right;
                    ti=0;
                    break;
            }
        }
    }

    int press=0;//蛇方向代表的整数
    //蛇的控制
    public void keyPress(KeyEvent e)
    {
        switch (this.snakeDirection){
            case Left:if(e.getKeyCode()!=KeyEvent.VK_RIGHT)press=e.getKeyCode();
            else {press=KeyEvent.VK_RIGHT;ti=1;}
            break;
            case Right:if(e.getKeyCode()!=KeyEvent.VK_LEFT)press=e.getKeyCode();
            else {press=KeyEvent.VK_LEFT;ti=1;}
            break;
            case Up:if(e.getKeyCode()!=KeyEvent.VK_DOWN)press=e.getKeyCode();
            else {press=KeyEvent.VK_DOWN;ti=1;}
            break;
            case Down:if(e.getKeyCode()!=KeyEvent.VK_UP)press=e.getKeyCode();
            else {press=KeyEvent.VK_UP;ti=1;}
            break;
        }
        //根据按键的整数值来改变蛇的方向
        switch (press) {
            case KeyEvent.VK_LEFT:
                this.snakeDirection = Direction.Left;
                break;
            case KeyEvent.VK_RIGHT:
                this.snakeDirection = Direction.Right;
                break;
            case KeyEvent.VK_UP:
                this.snakeDirection = Direction.Up;
                break;
            case KeyEvent.VK_DOWN:
                this.snakeDirection = Direction.Down;
                break;
        }
    }

    //与蛇相关的一切行为在这里发生
    public void paint(Graphics g){
        for(SnakeBody sbt : It){
            //如果是尾元素，渲染成黄色，集合尾部元素是蛇头
            if(It.peekLast().equals(sbt)){
                g.setColor(Color.yellow);
                g.fillRect(sbt.x, sbt.y, 20,20);
            }
            else{
                g.setColor(Color.blue);
                g.fillRect(sbt.x, sbt.y, 20,20);
            }
        }
        movel();//蛇移动
        huitou();//蛇掉头
        //eatBody();//蛇吃到身体
        zhuangqiang();//蛇撞墙
        eatFood(this.sc.food);//是否吃到食物
    }

    //蛇吃到身体
    public void eatBody(){
        //遍历蛇身除了头每一个节点
        //如果蛇头的位置和蛇身的位置重合，那么蛇死亡
        for(int i=0;i<It.size()-1;i++){
            if(getHeadRec().intersects(new Rectangle(It.get(i).x,It.get(i).y,20,20)))
                this.isLive=false;
        }
    }

    //撞墙检测
    //蛇一个节点20*20 地图900 * 800 边界大概宽度4，标题栏大概高度23
    public void zhuangqiang(){
        //当头节点碰到边界时，蛇死亡
        //要额外给一个节点的宽度，这样才能判断蛇头是否碰到边界
        if(It.peekLast().x<4-20 || It.peekLast().y<23-20+40||It.peekLast().x>877+20||It.peekLast().y>777+20)
        {
            //蛇死亡,计分板提示开始变色
            this.isLive=false;
            sc.lbl.setText("游戏结束，你的得分是："+this.eatEggs);
            sc.lbl.setBackground(Color.red);
        }
    }

    //蛇吃食物
    public void eatFood(Food fd){
        //如果蛇头的位置和食物的位置重合，那么蛇吃到食物
        if(this.getRec().intersects(fd.getRect())){
            eatEggs++;//吃到食物，得分加1
            sc.lbl.setText("得分："+this.eatEggs);//更新得分
            //获取旧的头元素
            SnakeBody bodyold = It.peekFirst();
            //集合头部插入新节点
            It.addFirst(new SnakeBody());
            //新节点的位置是旧的头元素的位置
            SnakeBody bodynew = It.peekFirst();
            switch(this.snakeDirection){
                //头节点坐标更新
                //往上走，x轴不变，y轴加长一格+20
                case Up:
                    bodynew.x = bodyold.x;
                    bodynew.y = bodyold.y+20;
                    break;
                case Down:
                    bodynew.x = bodyold.x;
                    bodynew.y = bodyold.y-20;
                    break;
                    //往下走，x轴不变，y轴减短一格-20
                case Left:
                    bodynew.x = bodyold.x-20;
                    bodynew.y = bodyold.y;
                    break;
                    //往左走，x轴减短一格-20，y轴不变
                case Right:
                    bodynew.x = bodyold.x+20;
                    bodynew.y = bodyold.y;
                    break;
                    //往右走，x轴加长一格+20，y轴不变
            }
            //食物的位置更新
            sc.food.reFood();
        }
    }

    //返回蛇头上一节的区域，用来检测是否吃到食物
    public Rectangle getRec(){
        return new Rectangle(It.get(It.size()-2).x,It.get(It.size()-2).y,It.peekFirst().width,It.peekFirst().height);
    }

    //返回蛇头区域
    public Rectangle getHeadRec(){
        return new Rectangle(It.peekLast().x,It.peekLast().y,20,20);
    }
}