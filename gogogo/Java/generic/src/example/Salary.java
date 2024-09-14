package example;

public class Salary <t1 extends Number,t2 extends Number>{
    t1 basepay;
    t2 bonus;

    public t1 getBasepay() {
        return basepay;
    }

    public void setBasepay(t1 basepay) {
        this.basepay = basepay;
    }

    public t2 getBonus() {
        return bonus;
    }

    public void setBonus(t2 bonus) {
        this.bonus = bonus;
    }
    public void diplay(){
        System.out.println("基本工资:"+basepay+",奖金:"+bonus);
    }
}
