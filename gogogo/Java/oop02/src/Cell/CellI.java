
public class CellI  extends CellFather{

    CellI cellI;
    CellI() {
        c[0] = new Cell();
        c[1] = new Cell();
        c[2] = new Cell();
        c[3] = new Cell();
    }
    CellI(int a,int b)
    {
        c[0] = new Cell(a,b);
        c[1] = new Cell(a+1,b);
        c[2] = new Cell(a+2,b);
        c[3] = new Cell(a+3,b);
    }
    
}
