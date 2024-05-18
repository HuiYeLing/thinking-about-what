#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        // dp数组用于存储到当前房屋为止能抢到的最大金额
        int dp[100]={0};
        
        // 如果没有房屋，返回0
        if (nums.size()==0)
        {
            return 0;
        }
        // 如果只有一个房屋，返回该房屋的金额
        if (nums.size()==1)
        {
            return nums[0];
        }
        // 如果有两个房屋，返回金额较大的那个
        if (nums.size()==2)
        {
            return max(nums[0],nums[1]);
        }
        // 初始化dp数组的前两个元素
        dp[0]=nums[0];
        dp[1]=max(nums[0],nums[1]);
        // 对于每个房屋，可以选择抢劫它，然后加上前一个房屋的最大金额
        // 或者选择不抢劫它，保持前一个房屋的最大金额
        for (int i = 2; i < nums.size(); i++)
        {
            dp[i]=max(dp[i-1],dp[i-2]+nums[i]);
        }
        // 返回最后一个房屋的最大金额
        return dp[nums.size()-1];
    }
};