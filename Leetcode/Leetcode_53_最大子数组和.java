class 最大子数组和_53 {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int result = dp[0];
        for (int i = 1; i < nums.length; i++){
            dp[i] = Integer.max(dp[i - 1] + nums[i], nums[i]);
            result = Integer.max(result, dp[i]);
        }
        return result;
    }
}