/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    if (nums.length == 1) return 0
    let idx = 0
    let ans = 0
    let jump, maxJump,nidx
    while (idx <= nums.length){
        ans += 1
        jump = nums[idx]+idx
        if (jump >= nums.length-1) return ans
        maxJump = 0
        nidx = idx
        for (let i=idx; i<=jump; i++){
            if (i >= nums.length) break
            if (maxJump < i+nums[i]){
                nidx = i
                maxJump = i+nums[i]
            }
        }
        if (nidx >= nums.length-1){
            return ans
        }
        idx = nidx
    }
    
    
};