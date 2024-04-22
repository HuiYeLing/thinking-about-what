#include <stdio.h>  
#include <stdlib.h>  
#define ListSize 10
typedef int DataType;

typedef struct 
{
    int data[ListSize];
    int length;
}SeqList;

void InsertList(SeqList *L,DataType x,int i)//����Ԫ��
{
    int j;
    if (i<1||i>L->length+1||L->length-1>=ListSize)
    {
        printf("�Ƿ�λ��");
        return;
    }
    for ( j = L->length; j >= i-1; j--)//��Ԫ�غ��ƣ�Ϊ��Ԫ�� x �ڳ�λ��
    {
        L->data[j+1]=L->data[j];//�����ƣ������������ڵ�Ե�
    }
    L->data[i-1]=x;//����x
    L->length++;
}

void DeleteList(SeqList *L,int i)
{
     int j;
    if (i<1||i>L->length)
    {
        printf("�Ƿ�λ��");

        return;
    }
    for ( j = i; j <= L->length; j++)
    {
        L->data[j-1]=L->data[j];//�ڵ�ǰ��
    }
    L->length--;//����С
}

int main() {  
int i; 
    SeqList L = {{0}, 4};  // ��ʼ�� L  
    printf("�������µ�Ԫ��ֵ\n");  
    for (i = 0; i < L.length; i++) {  
        int value;  
        scanf("%d", &value);  // ��ȡ�û������ֵ  
        L.data[i] = value;      // ���������е�ֵ  
    }  
    // ������º������Ԫ��  
    printf("���º������Ԫ��Ϊ��");  
    for (i = 0; i < L.length; i++) {  
        printf("%d ", L.data[i]);  
    }  
    printf("\n");  
    
    int x,k;
    printf("������x�����������,��i��������λ��\n"); 
    scanf("%d%d",&x,&i);
    InsertList(&L,x,i);
    for (k = 0; k < L.length; k++) {  
    printf("%d ", L.data[k]);  
    }  
    printf("\n");  
    return 0;  
}
