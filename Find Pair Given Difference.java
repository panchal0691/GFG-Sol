class Solution {
    public int findPair(int n, int x, int[] arr) {
        // code here
        HashSet<Integer> set=new HashSet<>();
        
        for(int a:arr){
            if(set.contains(a+x) || set.contains(a-x)) return 1;
            set.add(a);
        }
        
        return -1;
    }
}
