/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */

var leastInterval = function(tasks, n) {
    let freqArr = Array(26).fill(0)
    tasks.forEach(val=>{
        let ap = val.charCodeAt(0) - 65
        freqArr[ap] += 1
    })
    
    freqArr = freqArr.map((val,idx)=> {
        return [val, idx]
    })
    
    freqArr.sort((a,b)=>{
        return b[0] - a[0]
    })
    
    let ans = 0
    let empt = 0
    let term = 0
    freqArr.forEach(([val,idx])=>{
        if (!ans){
            ans += (val-1) * (n+1) + 1
            empt = (val-1) * n
            term = (val-1)
        } else {
            if (val > term){
                ans += 1
                val -= 1
            }
            if (empt >= val){
                empt -= val
            } else {
                ans += val - empt
                empt = 0
            }    
        }    
    })
    
    return ans
};