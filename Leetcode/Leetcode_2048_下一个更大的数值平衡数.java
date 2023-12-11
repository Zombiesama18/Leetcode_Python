package Leetcode;

public class 下一个更大的数值平衡数_2048 {
    public int nextBeautifulNumber(int n){
        for (int i = n + 1; i <= 1224444; i++){
            if (isBalance(i)) return i;
        }
        return -1;
    }
    public boolean isBalance(int n){
        int[] counter = new int[10];
        while (n > 0){
            counter[n % 10] += 1;
            n /= 10;
        }
        for (int i = 0; i < counter.length; i++){
            if (counter[i] > 0 && counter[i] != i){
                return false;
            }
        }
        return true;
    }
}
