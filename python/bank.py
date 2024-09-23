def account(name,number,balance):
    return {"name":name,"number":number,"balance":balance}
def deposit(acc,amount):
    if amount<=0:
        print("存款金额不能为负数")
    else:
        acc['balance']+=amount
def withdraw(acc,amount):
    if amount>acc["balance"]:
        print("余额不足")
    else:
        acc["balance"]-=amount
def describe(acc):
    return "AccountImformation:"+str(acc)
