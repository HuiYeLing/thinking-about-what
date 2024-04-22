#include <stdio.h>  
#include <stdlib.h>  
#define ListSize 10
typedef int DataType;

typedef struct 
{
    int data[ListSize];
    int length;
}SeqList;

void InsertList(SeqList *L,DataType x,int i)//插入元素
{
    int j;
    if (i<1||i>L->length+1||L->length-1>=ListSize)
    {
        printf("非法位置");
        return;
    }
    for ( j = L->length; j >= i-1; j--)//将元素后移，为新元素 x 腾出位置
    {
        L->data[j+1]=L->data[j];//结点后移，将相邻两个节点对调
    }
    L->data[i-1]=x;//插入x
    L->length++;
}

void DeleteList(SeqList *L,int i)
{
     int j;
    if (i<1||i>L->length)
    {
        printf("非法位置");

        return;
    }
    for ( j = i; j <= L->length; j++)
    {
        L->data[j-1]=L->data[j];//节点前移
    }
    L->length--;//表长减小
}

int main() {  
int i; 
    SeqList L = {{0}, 4};  // 初始化 L  
    printf("请输入新的元素值\n");  
    for (i = 0; i < L.length; i++) {  
        int value;  
        scanf("%d", &value);  // 读取用户输入的值  
        L.data[i] = value;      // 更新数组中的值  
    }  
    // 输出更新后的数组元素  
    printf("更新后的数组元素为：");  
    for (i = 0; i < L.length; i++) {  
        printf("%d ", L.data[i]);  
    }  
    printf("\n");  
    
    int x,k;
    printf("请输入x你想输入的数,和i你想插入的位置\n"); 
    scanf("%d%d",&x,&i);
    InsertList(&L,x,i);
    for (k = 0; k < L.length; k++) {  
    printf("%d ", L.data[k]);  
    }  
    printf("\n");  
    return 0;  
}
