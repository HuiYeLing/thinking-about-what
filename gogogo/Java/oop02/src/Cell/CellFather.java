public class CellFather {
    Cell[] c=new Cell[4];
    CellFather()
    {
        c[0]=new Cell();
        c[1]=new Cell();
        c[2]=new Cell();
        c[3]=new Cell();
    }
    boolean isMoveLeft()
    {
        for(int i=0;i<c.length;i++)
        if(c[i].col==1)
            return false;
    return true;
    }
    void moveleft()
    {
        if(isMoveLeft())
        {
            for(int i=0;i<c.length;i++)
            c[i].moveleft();
        }
    }
    boolean isMoveRight()
    {
        for(int i=0;i<c.length;i++)
            if(c[i].col==c[i].maxCol)
                return false;
        return true;
    }
    void moveright()
    {
        if(isMoveRight())
        {
            for(int i=0;i<c.length;i++)
            c[i].moveright();
        }
    }
    boolean isDrop()
    {
        for(int i=0;i<c.length;i++)
            if(c[i].row==c[i].maxRow)
                return false;
        return true;
    }

    void drop()
    {
        if(isDrop())
        {
            for(int i=0;i<c.length;i++)
            c[i].drop();
        }
    }
    boolean isEnabled(int x,int y)
    {
        //(x,y)是否在c[0] c[1] c[2] c[3]中,若是true，否则false
        for(int i=0;i<c.length;i++)
            if(x==c[i].row&&y==c[i].col)
                return true;
        return false;
    }
    void printCell()
    {
        for(int i=1;i<=c[0].maxRow;i++)
        {
            for(int j=1;j<=c[0].maxCol;j++)
            {
                if(isEnabled(i,j))
                    System.out.print("*");
                else
                    System.out.print("-");
            }
                System.out.println();
        }
    }
}
