#include<stdio.h>
int main()
{
int i,j,m;
scanf("%d",&m); 
	for(i=1;i<=m;i++)
{
	for (j=1;j<=i;j++)
	printf("%d*%d=%d ",i,j,i*j);
printf("\n");
}

return 0;
}
