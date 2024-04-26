class Solution {
    public int numberOfSteps(int num) {
        
        while(num>1)
        {
            num/2;
            num--;
            count++;
        }
    }
}