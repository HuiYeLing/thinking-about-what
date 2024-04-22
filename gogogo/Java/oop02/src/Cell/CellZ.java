public class CellZ extends CellFather{
    CellZ cellZ;
    CellZ() {
        c[0] = new Cell();
        c[1] = new Cell();
        c[2] = new Cell();
        c[3] = new Cell();
    }
    CellZ(int a,int b)
    {
        c[0] = new Cell(a,b);
        c[1] = new Cell(a,b+1);
        c[2] = new Cell(a+1,b+1);
        c[3] = new Cell(a+1,b+2);
    }
}
