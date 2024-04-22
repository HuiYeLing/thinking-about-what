#include<stdio.h>

typedef struct 
{
    DataType data[StackSize];
    int top;
}SeqStack;

void InitStack(SeqStack *S) //初始化栈,栈顶指针置-1,表示空栈
{
    S->top = -1;
}

int StackEmpty(SeqStack *S) //判断栈是否为空
{
    return S->top == -1;
}

int StackFull(SeqStack *S) //判断栈是否为满
{
    return S->top == StackSize - 1; //StackSzie为栈的最大容量
}  

void Push(SeqStack *S, DataType x) //进栈
{
    if(StackFull(S))
    {
        printf("栈满");//栈满上溢出
    }
        S->top++;//栈顶指针加1
        S->data[S->top] = x;//将x放入栈顶元素中
}

DataType Pop(SeqStack *S) //出栈
{
    DataType x;
    if (StackEmpty(S))
    {
        printf("栈空");//栈空下溢出
    }
        x = S->data[S->top];//取栈顶元素
        S->top--;//栈顶指针减1
        return x;//返回栈顶元素
}

DataType GetTop(SeqStack *S) //取栈顶元素
{
    if (StackEmpty(S))
    {
        printf("栈空");//栈空下溢出
    }
        return S->data[S->top];//返回栈顶元素
}