//Problem No. 268 - Missing NUmber
// package Arrays;

import java.util.Arrays;

public class missingnum {
    class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int x=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==x){
                x++;
            }
        }
        return x;
    }
} 
}
