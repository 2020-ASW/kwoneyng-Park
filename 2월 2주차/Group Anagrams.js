/**
 * @param {string[]} strs
 * @return {string[][]}
 */


var groupAnagrams = function(strs) {
    const ht = {}
    strs.forEach(str=>{
        let alpha = Array(26).fill(0)
        for (let i=0; i<str.length; i++){
            alpha[str.charCodeAt(i)-'a'.charCodeAt()] += 1
        }
        target = alpha.join()
        if (ht[target]){
            ht[target].push(str)
        } else{
            ht[target] = []
            ht[target].push(str)
        }
    })
    let keys = Object.keys(ht)
    const ans = Array(keys.length)
    for (let i=0; i<keys.length; i++){
        ans[i] = []
    }
    keys.forEach((key,idx)=>{
        ht[key].forEach(val=>{
            ans[idx].push(val)
        })
    })
    
    return ans
};