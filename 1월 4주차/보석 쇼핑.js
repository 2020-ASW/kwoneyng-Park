function solution(gems) {
    var ans = [];
    var maxl = 9999999
    var total = new Set(gems).size
    console.log(total)
    var ht = {}
    var n = 0
    var start = 0
    gems.forEach((item,idx)=>{
        if (!ht[item]){
            n += 1
            ht[item] = 1
        } else {
            ht[item] += 1
        }
        if (n == total){
            while (true){
                if (ht[gems[start]] == 1) break
                ht[gems[start]] -= 1
                start += 1
            }
            if (idx-start < maxl){
                maxl = idx-start
                ans = [start+1,idx+1]
            }
        }
    })
    return ans;
}