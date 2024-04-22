import java.util.Scanner;
public class CellDemo {
    public static void main(String[] args) {
        //创建一个小方块对象，赋属性，调用方法
        int t=(int)(Math.random()*7+1);
        CellJ c1=new CellJ(3,4);
        CellFather cf=new CellFather();
        switch (t){
            
            case 1:cf=new CellL(3,4);
            break;
            case 2:cf=new CellO(3,4);
            break;
            case 3:cf=new CellT(3,4);
            break;
            case 4:cf=new CellZ(3,4);
            break;
            case 5:cf=new CellI(3,4);
            break;
            case 6:cf=new CellJ(3,4);
            break;
        }
        //c1.row=3;
        //c1.col=4;由于构造方法，不需要在此赋初值
        System.out.println("place");
        c1.printCell();
        int command=4;
        while(command!=3)
        {
            System.out.println("请选择操作：1-左移，2-右移，0-下落,3-退出");
            Scanner scan=new Scanner(System.in);
            command=scan.nextInt();
            switch(command)
            {
                case 0:
                    c1.drop();
                    c1.printCell();
                    break;
                case 1:
                    c1.moveleft();
                    c1.printCell();
                    break;
                case 2:
                    c1.moveright();
                    c1.printCell();
                    break;
                case 3:
                    System.out.println("退出");
                    break;
                default:System.out.println("输入错误");
            }
        }
    }
}