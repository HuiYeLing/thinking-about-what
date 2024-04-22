#include<bits/stdc++.h>
using namespace std;
int main()
{
        long long int n;
        cin >> n;
        long long int a[n][n]={0}; // 创建一个二维数组a来表示棋盘
        for (int  i = 0; i < n; i++)
        {
            for (int  j = 0; j < n; i++)
            cin >>  i,j,a[i][j]; // 读入棋盘的每一个点的值
        }
        for (int  i = 0; i <=n; i++) // 遍历棋盘的每一行
        {
                for ( int j = 0; j <=n; j++) // 遍历棋盘的每一列
                {
                     if (i==0 && j==0) // 如果是棋盘的左上角，跳过
                     {
                         continue; 
                     }
                     if (i==0) // 如果在第一行，只能从左边来
                     {
                       a[i][j]=a[i][j-1];
                     }  
                     else if (j==0) // 如果在第一列，只能从上边来
                     {
                        a[i][j]=a[i-1][j];
                     }
                     else // 其他情况，可以从左边或上边来
                        {
                         a[i][j]=a[i-1][j]+a[i][j-1];
                        }
                }
                
        }
        cout << a[n][n]; // 输出从棋盘的左上角到右下角的所有可能路径的数量
}