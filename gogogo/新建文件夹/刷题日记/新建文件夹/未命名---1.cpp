#include <stdio.h>  
#include <stdlib.h>  
  
// �ȽϺ�������������  
int cmp(const void *a, const void *b) {  
    return *(char *)b - *(char *)a;  
}  
  
// ɾ�����ֺ���  
void deleteDigits(int n, int k) {  
    char num[n + 1]; // �洢���ֵ��ַ�����  
    int len = n - k; // ɾ��k�����ֺ�������ֳ���  
    for (int i = 0; i < n; i++) {  
        num[i] = '0' + (n % 10); // ������ת��Ϊ�ַ����洢��������  
        n /= 10;  
    }  
    num[n] = '\0'; // ����ַ�����β��־  
    qsort(num, len, sizeof(char), cmp); // �������������  
    printf("������Ϊ��");  
    for (int i = 0; i < len; i++) {  
        printf("%c", num[i]); // ���������  
    }  
    printf("\n");  
}  
  
int main() {  
    int n, k;  
    scanf("%d%d", &n, &k);  
    deleteDigits(n, k);  
    return 0;  
}
