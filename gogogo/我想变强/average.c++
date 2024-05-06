#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
class Solution {
public:
    double average(vector<int>& salary) {
        double sum=0;
        double  max=*max_element(salary.begin(),salary.end());
        double  min=*min_element(salary.begin(),salary.end());
        for (int i = 0; i < salary.size(); i++)
        {
            sum=sum+salary[i];
        }
        return (sum-max-min)/(salary.size()-2);

}
};