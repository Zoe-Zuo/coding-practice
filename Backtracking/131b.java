public class Solution {
    public List<List<String>> partition(String s) {
        /**
         * is Pal(a[i->j]) = isPal(a[i+1->j-1]) && a[i] == a[j]
         * base case:
         * isPal(a[i->i+1]) = a[i] == a[j]
         * isPal(a[i->i])= true;
         */
        boolean[][] isPal = getPal(s);
        //List<List<String>>[]
        List<List<List<String>>> allResults = new ArrayList<>();
            for (int i = 0; i<s.length(); i++) {
                allResults.add(null);
            }
            helper(s, s.length()-1, allResults, isPal);
            return allResults.get(s.length()-1);
    }
    
    private void helper(String s, int end, List<List<List<String>>> allResults, boolean[][] isPal){
        if (allResults.get(end) !=null){
            return;
        }
        
        List<List<String>> result = new ArrayList<>();
        
        if (isPal[0][end]){
            List<String> list = new ArrayList<>();
            //result.add(lists.of(s.substring(0, end+1)));
            list.add(s.substring(0, end + 1));
            result.add(list);
        }
        
        for (int p = 1; p <= end; p++) {
            if(isPal[p][end]){
                helper(s, p-1, allResults, isPal);
                List<List<String>> preResult = allResults.get(p - 1);
                for (List<String> preList : preResult){
                    List<String> curList = new ArrayList<>(preList);
                    curList.add(s.substring(p, end + 1));
                    result.add(curList);
                }
            }
        }
        
        allResults.set(end,result);
    }
    private boolean[][] getPal(String s){
        final int n = s.length();
    boolean[][]isPal = new boolean[n][n];
        for ( int level = 0; level < n; level++){
            for (int diag = 0; diag<=n-1-level; diag++){
                int i = diag;
                int j = level+diag;
                
                if (j==i){
                    isPal[i][j] = true;
                }else if(j==i+1){
                    isPal[i][j] = s.charAt(i) == s.charAt(j);
                }else{
                    isPal[i][j] = (s.charAt(i) == s.charAt(j)) && isPal[i+1][j-1];
                }
            }
        }
        
        return isPal;
    }
}
            
            
        
    