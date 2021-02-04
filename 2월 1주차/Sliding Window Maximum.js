function bnsearch(x,arr){
    let l=0, r=arr.length-1
    while (l<=r){
        let m=parseInt((l+r)/2)
        if (x > arr[m]){
            l = m + 1
        } else {
            r = m-1
        }
    }
    return l
}



var maxSlidingWindow = function(nums, k) {
    const que = []
    const ans = []
    for (let i=0; i<k; i++){
        que.push(nums[i])
    }
    que.sort((a,b)=>{
        return a-b
    })
    ans.push(que[que.length-1])
    // console.log(que)
    for (let i=k; i<nums.length; i++){
        let didx = bnsearch(nums[i-k],que)
        que.splice(didx,1)
        let nidx = bnsearch(nums[i],que)
        if (nidx == k){
            que.push(nums[i])
        } else {
            que.splice(nidx,0,nums[i])
        }
        ans.push(que[que.length-1])
        // console.log(que)
    }
    return ans
};