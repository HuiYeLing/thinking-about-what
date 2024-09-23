import bank
acc1=bank.account("tom","123-4567",1000)
bank.deposit(acc1,500)
print(bank.describe(acc1))
bank.withdraw(acc1,100)
print(bank.describe(acc1))