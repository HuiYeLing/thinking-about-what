def func_immutable(aXC):
    aXC=10
aSC=4
func_immutable(aSC)
print(aSC)

def func5(a,b):
    c=a+b
    return c 
func5(6,3)

def printinfo(name,age):
    print("名字",name)
    print("年龄",age)
    return
printinfo(age=50,name="tom")

def f_3(name,*hobby):
    print('name:{0}'.format(name))
    print('hobby:{0}'.format(hobby))

f_3('tom','swimming','reading','game')
