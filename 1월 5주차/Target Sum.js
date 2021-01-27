/**
 * @param {number[]} nums
 * @param {number} S
 * @return {number}
 */
function dfs(nums, s, idx=0, rs=0){
    if (idx==nums.length){
        if (rs == s) ans += 1
        return
    }
    dfs(nums,s,idx+1,rs+nums[idx])
    dfs(nums,s,idx+1,rs-nums[idx])
}

var ans
var findTargetSumWays = function(nums, S) {
    ans = 0
    let n = nums.length
    dfs(nums,S)
    return ans
};