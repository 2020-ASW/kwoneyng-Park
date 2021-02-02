/**
 * @param {number[]} nums
 * @return {number}
 */
function find(arr,x){
    if (!arr.length){
        return 0
    }
    let l,r,m
    l = 0
    r = arr.length-1
    while(l<=r){
        m = parseInt((l+r)/2)
        if (arr[m] >= x){
            r = m - 1
        } else {
            l = m + 1
        }
    }
    return l
}


var lengthOfLIS = function(nums) {
    let ans = []
    nums.forEach(x=>{
        let sit = find(ans,x)
        if (sit == ans.length){
            ans.push(x)
        } else{
            ans[sit] = x
        }
    })
    
    return ans.length
};