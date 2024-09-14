package example;

public class TestPointsalary {
    public static void main(String[] args){
        Salary<Integer,Float>s1 = new Salary<Integer,Float>();
        s1.setBasepay(3000);
        s1.setBonus(1080.5f);
        s1.diplay();
        Salary<Double,Double>s2 = new Salary<Double,Double>();
        s2.setBasepay(6080.2);
        s2.setBonus(5005.5);
        s2.diplay();
    }
}
