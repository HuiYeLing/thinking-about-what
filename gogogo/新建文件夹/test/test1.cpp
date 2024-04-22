#include<bits/stdc++.h>
using namespace std;
int main()
{
	int k;
	cin>>k;
	int sub1,sub2,sub3;
	for (int i = 9999; i <=30000; i++)
	{
		sub1=i/100;
		sub2=i/10%1000;
		sub3=i%1000;
		if(sub1%k==0 && sub2%k==0 && sub3%k==0)
		{
			cout<<i<<endl;
		}
		else
			cout<<"No"<<endl;
	}
	
}