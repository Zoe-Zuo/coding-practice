public class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dictSet = wordDict.stream().collect(Collectors.toSet());
        
        //List<String>[]
        List<List<String>> allResults = new ArrayList<>();
        for ( int i =0; i<=s.length(); i++){
            allResults.add(null);
        }
        helper(s, s.length()-1, dictSet, allResults);
        return allResults.get(s.length()-1);
        
    }
    private void helper(String s, int end, Set<String> dict, List<List<String>> allResults){
        if (allResults.get(end)!=null){
            return;
        }
        
        List<String> result =new ArrayList<>();
        
        if (dict.contains(s.substring(0, end+1))){
            result.add(s.substring(0, end+1));
        }
        
        for (int p=1; p<=end; p++){
            if (dict.contains(s.substring(p, end+1))){
                helper(s, p-1, dict, allResults);
                for (String preString: allResults.get(p-1)){
                    result.add(preString + " " + s.substring(p, end+1));
                }
            }
        }
        allResults.set(end, result);//allResults[end]=result;
    }
    
}