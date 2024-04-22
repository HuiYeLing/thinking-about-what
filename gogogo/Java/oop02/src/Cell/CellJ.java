
public class CellJ extends CellFather{
    CellJ cellJ;
    CellJ()
    {
        c[0]=new Cell();
        c[1]=new Cell();
        c[2]=new Cell();
        c[3]=new Cell();
    }
    //сп╡н
    CellJ(int a,int b)
    {
        c[0]=new Cell(a,b);
        c[1]=new Cell(a+1,b);
        c[2]=new Cell(a+2,b-1);
        c[3]=new Cell(a+1,b-2);
    }
    
}
