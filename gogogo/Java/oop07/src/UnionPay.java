public interface UnionPay {    
    //声明接口            
    public boolean checkPwd(String inputword);//检查密码
    public boolean drawMoney(double outmoney);//取款
    public double getMoney();//查询余额


}
