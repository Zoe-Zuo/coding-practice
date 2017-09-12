public class Solution {
    public int numDecodings(String s) {
        if(s.length()==0){
            return 0;
        }
        
        //i:-1
        int pre2 = 1;
        
        //i:0
        if (s.charAt(0)=='0'){
            return 0;
        }
        int pre1 = 1;
        
        //i:1->n-1
        for (int i = 1; i<s.length(); i++){
            int cur = 0;
            if (s.charAt(i)!= '0'){
                cur+=pre1;
            }
            int val = Integer.valueOf(s.substring(i-1, i+1));
            if(10 <= val && val<=26) {
                cur += pre2;
            }
            pre2 = pre1;
            pre1 = cur;
        }
        
        return pre1;
    }
}