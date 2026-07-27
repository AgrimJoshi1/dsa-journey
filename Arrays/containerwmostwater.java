// package Arrays;

public class containerwmostwater {
    class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;

        for (int i = 0; i < height.length - 1; i++) {
            for (int j = i + 1; j < height.length; j++) {
                int width = j - i;
                int h = Math.min(height[i], height[j]);
                int area = width * h;

                if (area > maxArea) {
                    maxArea = area;
                }
            }
        }

        return maxArea;
    }
}
    
}
