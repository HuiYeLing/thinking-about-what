
public class CellT extends CellFather{
    CellT cellT;
    CellT()
     {
        super();
         c[0]=new Cell();
         c[1]=new Cell();
         c[2]=new Cell();
         c[3]=new Cell();
     }
     //сп╡н
     CellT(int a,int b)
     {
        super();
         c[0]=new Cell(a,b);
         c[1]=new Cell(a,b+1);
         c[2]=new Cell(a,b+1);
         c[3]=new Cell(a,b+1);
     }
    
 }
 