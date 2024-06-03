import java.util.Scanner;

public class mnarr {
  
    static Scanner scan = new Scanner(System.in);
    static int m=0;//行数
    static int n=0;//列数
    static int row=0;
    static int column=0;
    
    static int right=0;
    static int down=1;
    static int left=2;
    static int up=3;
    static int [][] arr=null;
    static int direction=right;
    static int circle=1;
    static int count=0;
    public static void input()
    {
        System.out.println("请输入行数：");
        m=scan.nextInt();
        System.out.println("请输入列数：");
        n=scan.nextInt();
        arr=new int[m][n];
    }
    //填充二维数组
   public static void fillArray()
{
    while(count<m*n)
    {
        count++;
        arr[row][column]=count;         
        switch (direction) {
            case 0:
                if(column<n-circle) column++;
                else {direction=down; row++;}
                break;

            case 1:
                if(row<m-circle) row++;
                else {direction=left; column--;}
                break;

            case 2:
                if(column>circle-1) column--;
                else {direction=up; row--;}
                break;

            case 3:
                if(row>circle) row--;
                else {circle++; direction=right; column++;}
                break;
        }
    }
}
    //打印
    public static void printArray()
    {
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(arr[i][j]<10)
                    System.out.print(arr[i][j]+"  ");
                else
                    System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        input();
        fillArray();
        printArray();
    }
}