
public class Cell {
    int maxRow=10;
    int maxCol=10;
    int row;
    int col;
    
    //���췽�� ����ֵ
    Cell()
    {
        row=3;
        col=4;
    }
    //�вι��췽��
    Cell(int r,int c)
    {
        row=r;
        col=c;
    }
    
    void moveleft()
    {
        if(col>1)
        col--;
    }
    void moveright()
    {
        if(col<maxCol)
        col++;
    }
    void drop()
    {   
        if(row<maxRow)
        row++;
    }
    void getCellInfo()
    {
        System.out.println("row:"+row+"col:"+col);
    }
    void printCell()
    {
        for(int i=1;i<=maxRow;i++)
        {
            for(int j=1;j<=maxCol;j++)
            {
                if(i==row&&j==col)
                    System.out.print("*");
                else
                    System.out.print("-");
            }
                System.out.println();
        }
    }
}

