class Solution {
    public boolean isPalindrome(int x) {
        int l = 0;
        int temp = x;
        
        
        while(x>0){
            int r = x % 10;
            l = l*10 + r;
            x =x / 10;
        }
        if(temp==l){
            return true;
        }
        return false;
    }
}