class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int temp = x;
        int n = s.length()-1;
        int l = 0;
        while(l<=n){
            if (s.charAt(l)!=s.charAt(n))
                return false;
            l++;
            n--;
        }
        return true;
    }
}