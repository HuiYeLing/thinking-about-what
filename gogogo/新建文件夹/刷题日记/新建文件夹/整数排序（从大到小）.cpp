#include<stdio.h>
int main()
{
  int N;
  scanf("%d",&N);
  int istu[N],i,k,itemp;
  for ( i = 0; i < N; i++)
    scanf("%d",&istu[i]);
  for ( k = 1; k <= N-1; k++)
{
    for ( i = N-1; i >=k; i--)
  { 
    if (istu[i]>istu[i-1])
    {
      itemp=istu[i];
      istu[i]=istu[i-1];
      istu[i-1]=itemp;
    }
  }
}
  for ( i = 0; i < N-1; i++)
  printf("%d ",istu[i]);
  printf("%d",istu[N-1]);
  return 0;
}
