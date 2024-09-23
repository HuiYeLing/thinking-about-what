def fact(n):
    if n== 1:
        return 1
    else:
        return n*fact(n-1)
if __name__=='__main__':
    n=int(input("请输入一个正整数:"))
    f=fact(n)
    print("{}的阶乘是:{}".format(n,f))

def selectsort(numbers):
    def findmin():
        min=i
        for j in range (i,len(numbers)):
            if numbers[j]<numbers[min]:
                min=j
        return min
    for i in range (len(numbers)):
        selected=findmin()
        if i!=selected:
                numbers[i],numbers[selected]=numbers[selected],numbers[i]
if __name__=='__main__':
    numbers=[45,6,2,64,6,9,1]
    print("未排序:{}".format(numbers))
    selectsort(numbers)
    print("排序后:{}".format(numbers))
    
    