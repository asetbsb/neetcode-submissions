class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> vals = new HashSet<>();
        for (int i : nums) {
            if (!vals.add(i)) {
                return true;
            }
        }
        return false;
    }
}