class Solution {
public:
    bool check(vector<int>& nums) {
        int breakpoints = 0;
        for(int i=1; i<nums.size();i++){
            if(nums[i]<nums[i-1]){
                breakpoints++;
            }
        }
        if(nums[nums.size()-1]>nums[0]){
            breakpoints++;
        }
        if(breakpoints==1 or breakpoints==0){
            return true;
        }
        else{
            return false;
        }
    }
};