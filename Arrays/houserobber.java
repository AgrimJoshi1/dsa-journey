public class houserobber {
    class Solution {
    public int rob(int[] nums) {
        int max1 = 0;
        int max2 = 0;

        for (int money : nums) {
            int temp = max1;

            max1 = Math.max(max1, max2 + money);

            max2 = temp;
        }

        return max1;
    }
}
}
