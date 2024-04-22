#include <stdio.h>  
#include <stdlib.h>  
  
#define ListSize 10  
typedef int DataType;  
  
typedef struct {  
    int data[ListSize];  
    int length;  
} SeqList;  
  
void InsertList(SeqList *L, DataType x, int i) { // ����Ԫ��  
    if (i < 1 || i > L->length + 1 || L->length >= ListSize) {  
        printf("�Ƿ�����\n");  
        return;  
    }  
    for (int j = L->length; j >= i - 1; j--) {  
        L->data[j] = L->data[j - 1]; // ������  
    }  
    L->data[i - 1] = x; // ����x  
    L->length++; // ������  
}  
  
void DeleteList(SeqList *L, int i) { // ɾ��Ԫ��  
    if (i < 1 || i > L->length) {  
        printf("�Ƿ�����\n");  
        return;  
    }  
    for (int j = i; j < L->length; j++) {  
        L->data[j - 1] = L->data[j]; // �ڵ�ǰ��  
    }  
    L->length--; // ����С  
}  
  
int main() {  
    SeqList L = {{0}, 4};  // ��ʼ�� L  
  
    printf("�������µ�Ԫ��ֵ\n", L.length);  
    for (int i = 0; i < L.length; i++) {  
        int value;  
        scanf("%d", &value);  // ��ȡ�û������ֵ  
        L.data[i] = value;      // ���������е�ֵ  
    }  
    // ������º������Ԫ��  
    printf("���º������Ԫ��Ϊ��");  
    for (int i = 0; i < L.length; i++) {  
        printf("%d ", L.data[i]);  
    }  
    printf("\n");  
    
    int x,i;
    printf("������x�����������,��i��������λ��\n"); 
    scanf("%d%d",&x,&i);
    InsertList(&L,x,i);
    for (int k = 0; k < L.length; k++) {  
    printf("%d ", L.data[k]);  
    }  
    printf("\n");  
    return 0;  
}
