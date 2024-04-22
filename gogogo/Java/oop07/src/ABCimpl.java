public class ABCimpl implements ICBC{
    private double money;
    private final String pwd;

    public ABCimpl() 
    {
        super();
        this.money = 10000;
        this.pwd = "123456";
    }
    public ABCimpl(final double money, final String pwd) 
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

    public boolean payTellBill(String number ,double tellmoney){
        if (this.money >=tellmoney) {
            this.money -= tellmoney;
            System.out.println("支付电话费成功，电话号码："+number+" 金额："+tellmoney+" 余额："+this.money);
            return true;
        }
        return false;
    }
}
