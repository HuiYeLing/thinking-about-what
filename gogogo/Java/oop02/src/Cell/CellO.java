public class CellO extends CellFather{
    CellO cellO;  
    CellO()
    {
        c[0]=new Cell();
        c[1]=new Cell();
        c[2]=new Cell();
        c[3]=new Cell();
    }
    //сп╡н
    CellO(int a,int b)
    {
        c[0]=new Cell(a,b);
        c[1]=new Cell(a,b+1);
        c[2]=new Cell(a+1,b);
        c[3]=new Cell(a+1,b+1);
    }
   
    
}
