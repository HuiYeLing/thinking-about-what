#include<stdio.h>

typedef struct 
{
    DataType data[StackSize];
    int top;
}SeqStack;

void InitStack(SeqStack *S) //��ʼ��ջ,ջ��ָ����-1,��ʾ��ջ
{
    S->top = -1;
}

int StackEmpty(SeqStack *S) //�ж�ջ�Ƿ�Ϊ��
{
    return S->top == -1;
}

int StackFull(SeqStack *S) //�ж�ջ�Ƿ�Ϊ��
{
    return S->top == StackSize - 1; //StackSzieΪջ���������
}  

void Push(SeqStack *S, DataType x) //��ջ
{
    if(StackFull(S))
    {
        printf("ջ��");//ջ�������
    }
        S->top++;//ջ��ָ���1
        S->data[S->top] = x;//��x����ջ��Ԫ����
}

DataType Pop(SeqStack *S) //��ջ
{
    DataType x;
    if (StackEmpty(S))
    {
        printf("ջ��");//ջ�������
    }
        x = S->data[S->top];//ȡջ��Ԫ��
        S->top--;//ջ��ָ���1
        return x;//����ջ��Ԫ��
}

DataType GetTop(SeqStack *S) //ȡջ��Ԫ��
{
    if (StackEmpty(S))
    {
        printf("ջ��");//ջ�������
    }
        return S->data[S->top];//����ջ��Ԫ��
}