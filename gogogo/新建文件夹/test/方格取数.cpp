#include<bits/stdc++.h>
using namespace std;
int main()
{
        long long int n;
        cin >> n;
        long long int a[n][n]={0}; // ����һ����ά����a����ʾ����
        for (int  i = 0; i < n; i++)
        {
            for (int  j = 0; j < n; i++)
            cin >>  i,j,a[i][j]; // �������̵�ÿһ�����ֵ
        }
        for (int  i = 0; i <=n; i++) // �������̵�ÿһ��
        {
                for ( int j = 0; j <=n; j++) // �������̵�ÿһ��
                {
                     if (i==0 && j==0) // ��������̵����Ͻǣ�����
                     {
                         continue; 
                     }
                     if (i==0) // ����ڵ�һ�У�ֻ�ܴ������
                     {
                       a[i][j]=a[i][j-1];
                     }  
                     else if (j==0) // ����ڵ�һ�У�ֻ�ܴ��ϱ���
                     {
                        a[i][j]=a[i-1][j];
                     }
                     else // ������������Դ���߻��ϱ���
                        {
                         a[i][j]=a[i-1][j]+a[i][j-1];
                        }
                }
                
        }
        cout << a[n][n]; // ��������̵����Ͻǵ����½ǵ����п���·��������
}