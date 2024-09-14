
public class Triangle {
    private double a,b,c;
  
    public Triangle(){
    }
    public Triangle(double a,double b,double c) 
    {
        super();
        this.a=a;
        this.b=b;
        this.c=c;
    }
    public void judgeTriangle() throws EdgeException{
        if(a<0||b<0||c<0){
            throw new EdgeException("三角形的边长不能为负数");
        }
        else if (a+b<=c || a+c<=b || b+c<=a){
            throw new EdgeException("三角形的两边之和必须大于第三边");
        }
        else{
            System.out.println("三角形的三边为："+a+"\t"+b+"\t"+c);
            
        }
    }
}
