#include<iostream>
#include<vector>
#include<algorithm>  
using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) 
    {
        int n=nums.size();
        for (int i = 1; i < n; i++)
        {
            nums[i]=nums[i]+nums[i-1];
            return nums;
        }
    
    }
};
int int main(int argc, char const *argv[])
{
    cin>>n;
    return 0;
}
