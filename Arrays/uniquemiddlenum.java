// package Arrays;

public class uniquemiddlenum {
    class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int m = nums[nums.length / 2];
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == m) {
                count++;
            }
        }

        return count == 1;
    }
}
}
