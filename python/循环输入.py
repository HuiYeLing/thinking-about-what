n=1
s=0
while n<=100:
    s=s+n
    n=n+1
print("1到100之间的整数和：%d"%(s))

#素数的判断
n=int(input("请输入一个整数"))
i=2
while i<n:
    if n%i==0:
        print("%d不是素数"%(n))
        break
    i+=1
else:
    print("%d是素数"%(n))

#判断一个字符串中是否有数字
string=input("请输入字符串")
for s in string:
    if s in '0123456789':
        print("字符串string=\"%s\"中，包含数字"%(string))
        break
else:
    print("字符串string=\"%s\"中，不包含数字"%(string))

numbers=[1,2,5,7,12,9,8]
for i in range(len(numbers)):
    numbers[i]=numbers[i]**2
    print(numbers[i],end=' ')

number1=[1,2,3,4,5]
names=['a','b','c','d','e']
genders=['male','female','female','male']
for item in zip(number1,names,genders):
    print(item)

websites={'1':'baidu','2':'genship impact','3':'zmezon','4':'google'}
for k in websites:
    print(k)
for item in websites.items():
    print(item)
for k,v in zip(websites.keys(),websites.values()):
    print("number:{}\twebsite:{}".format(k,v))

string=input("请输入一个字符串")
number2=0
for s in string:
    if s in '0123456789':
        number2+=1
    else:
        pass
print('\'%s\'字符串中的数字个数为:%d'%(string,number2))

student={'tom':23,'rose':21,"peter":14}
number3=0
for  k,v in zip(student.keys(),student.values()):
    if  v<= 20:
        continue
    print("name:{}\tage:{}".format(k,v))
    number3+=1
else:
    print("大于20岁的人数为:{}".format(number3))
