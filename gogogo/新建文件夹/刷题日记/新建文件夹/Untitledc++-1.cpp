#include<bits/stdc++.h>  
using namespace std;  
int main()
{
	int M,i,ws=0;
	string A;
	scanf("%d",&M);
	cin>>A;
	ws=A.size()-1;
	for ( i = 0; i < A.size()-1; i++)
	{
		if (A[i]!='0')
		{
			printf("%c*%d^%d+",A[i],M,ws);
		}
		ws--;
	}
	if (A[ws]!=0)
    {
        printf("%c*%d^%d",A[ws-1],M,ws);
    }
    

    return 0;
}