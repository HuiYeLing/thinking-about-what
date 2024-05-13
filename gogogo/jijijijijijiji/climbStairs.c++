#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
//普通递归方法
// class Solution {
// public:
//     int climbStairs(int n) {
//         vector<int> n(50);
//         if (n==1)
//         {
//             return 1;
//         }
//         if (n==2)
//         {
//             return 2;
//         }
        

//         return climbStairs(n-1)+climbStairs(n-2);
//     }
// };

//动态规划
class Solution {
public:
    int climbStairs(int n) {
        if (n==1)
        {
            return 1;
        }
        int dp[50];
        dp[1]=1;
        dp[2]=2;
        for (int i = 0; i < n; i++)
        {
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
};

