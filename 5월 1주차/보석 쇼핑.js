function solution(gems) {
    var answer = [];
    let total = new Set(gems).size
    console.log(total)
    const have = {}
    let cnt = 0
    let left = 0
    let min = 1/0
    gems.forEach((gem,idx)=>{
        if (have[gem]){
            have[gem]++
        } else{
            have[gem] = 1
            cnt++
        }
        if (cnt == total){
            while (have[gems[left]]-1){
                have[gems[left++]]--
            }
            if (min > idx-left){
                answer = [left+1,idx+1]
                min = idx-left
            }
        }
    })
    
    return answer;
}