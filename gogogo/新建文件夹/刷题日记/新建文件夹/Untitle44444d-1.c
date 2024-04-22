#include <stdio.h>  
const int maxsize=1005;//栈的大小  
  
typedef struct  
{  
    int data[maxsize];//存放栈里面的数据  
    int top;//一般保存栈顶元素的下标  
} Sqstack;  
  
void clear(Sqstack *s)  
{//初始化栈  
    s->top=-1;  
}  
  
bool stackempty(Sqstack *s)  
{//判断栈是否为空  
    if(s->top==-1) return true;  
    else return false;  
}  
  
bool push(Sqstack *s,int x)  
{//将x入栈  
    if(s->top==maxsize-1)//栈满，不能入栈  
        return false;  
    s->top=s->top+1;//下标上移一位  
    s->data[s->top]=x;//将x入栈  
    return true;  
}  
  
bool pop(Sqstack *s,int *x)  
{//出栈  
    if(s->top==-1) return false;  
    *x=s->data[s->top];  
    s->top=s->top-1;  
    return true;  
}  
  
void printstack(Sqstack *s)  
{  
    if (s->top == -1) { // 判断栈是否为空  
        printf("[]\n");  
        return;  
    }  
    printf("[");  
    while(!stackempty(s))  
    {     
        int x=-1;//用于保存出栈的值  
        pop(s,&x);  
        printf("%d ",x);//输出出站的值  
    }  
    printf("]\n");  
}  
  
int main()   
{  
    Sqstack s;  
    clear(&s);  
    push(&s,1);  
    push(&s,2);  
    push(&s,3);  
    push(&s,4);  
    push(&s,5);  
    push(&s,6);  
   	  
    printstack(&s); // 使用指针来传递栈对象，因为printstack函数需要修改栈的内容。  
   	  
    return 0;  
}