#include<stdio.h>
int main()
{
    char id[19];
    scanf_s("%s",id);
    int nian = (id[6] - '0') * 1000 + (id[7] - '0' )* 100 +( id[8] - '0') * 10 + (id[9] - '0');
    int yue =( id[10] - '0') * 10 + (id[11] - '0');
    int ri = (id[12] - '0' )* 10 +( id[13] - '0');
    printf("%d-%d-%d", nian, yue, ri);
    return 0;
}