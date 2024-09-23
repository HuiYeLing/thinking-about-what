input('请输入一个数字：')
a=123
b=34.1234
c='hello world'
print(a,b,c,sep=' ',end='\n')

print('%d\n%u\n%o\n%x'%(12,12,12,12))
print("%c\n%s\n%d"%('a','abc',12))
print('%f,%e,%g'%(1234.56789,1234.56789,12345.6789))
print('%f,%e,%g'%(1234.56789,1234.56789,1234567.89))
print('%-10.2f%-10.3f%10.1f'%(1234.56789,1234.56789,1234567.89))

print("{} {}".format("玩原神","废了"))
print("{0} {1}".format("玩原神","废了"))
print("{1} {0}".format("玩原神","废了"))

print("姓名:{name},年龄:{age},性别:{gender}".format(gender='male',name="tom",age="12"))