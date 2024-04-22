public class ICBCImpl implements ICBC{
    private double money;
    private final String pwd;

    public ICBCImpl() 
    {
        super();
        this.money = 10000;
        this.pwd = "123456";
    }
    public ICBCImpl(final double money, final String pwd) 
    {
        super();
        this.money = money;
        this.pwd = pwd;
    }
    

    @Override
    public boolean payOnline(final double onlineoutmoney) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean checkPwd(final String inputword) {
        // TODO Auto-generated method stub
        if(inputword.equals(this.pwd))
        return true;
        return false;
    }

    @Override
    public boolean drawMoney(final double outmoney) {
        // TODO Auto-generated method stub
        if (this.money >=outmoney) {
            this.money -= outmoney;
            return true;
        }
        return false;

    }

    @Override
    public double getMoney() {
        return this.money;
    }

    
    
}
