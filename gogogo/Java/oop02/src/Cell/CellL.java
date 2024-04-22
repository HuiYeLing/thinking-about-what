
public class CellL extends CellFather{
    CellL cellL;
    CellL()
    {
        c[0]=new Cell();
        c[1]=new Cell();
        c[2]=new Cell();
        c[3]=new Cell();
    }
    CellL(int a,int b)
    {
        c[0]=new Cell(a,b);
        c[1]=new Cell(a+1,b);
        c[2]=new Cell(a+1,b-1);
        c[3]=new Cell(a+1,b);
    }
    
}
